from datetime import timedelta, date

from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from borrow.models import Borrow
from borrow.api.serializer import BorrowSerializer

from reservation.models import Reservation
from notification.models import Notification


# Book borrow API
class BorrowView(GenericAPIView):

    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def get(self, request):

        borrows = Borrow.objects.all().order_by("-issued_at")

        serializer = BorrowSerializer(borrows, many=True)

        return Response(serializer.data, status=200)

    def post(self, request):

        serializer = BorrowSerializer(data=request.data)

        if serializer.is_valid():

            member = serializer.validated_data["member"]
            book = serializer.validated_data["book"]
            issued_by = serializer.validated_data.get("issued_by")

            # 🔐 member approval
            if not member.is_active:
                return Response({"error": "Member is not active"}, status=403)

            # 🔐 subscription check
            if not member.subscription:
                return Response({"error": "No active subscription"}, status=400)

            today = timezone.now().date()

            # 🔐 subscription expiry
            if member.subscription_end < today:
                return Response({"error": "Subscription expired"}, status=400)

            plan = member.subscription

            # ❌ duplicate active borrow
            already_borrowed = Borrow.objects.filter(
                member=member, book=book, is_returned=False
            ).exists()

            if already_borrowed:
                return Response({"error": "Book already borrowed"}, status=400)

            # 📚 borrow limit
            active_count = Borrow.objects.filter(
                member=member, is_returned=False
            ).count()

            if active_count >= plan.max_books:
                return Response({"error": "Borrow limit reached"}, status=400)

            # 📦 stock check
            if book.available_copies <= 0:
                return Response({"error": "Book not available"}, status=400)

            # ⬇ reduce stock
            book.available_copies -= 1
            book.save()

            # 📅 due date
            due_date = today + timedelta(days=plan.max_borrow_days)

            borrow = serializer.save(due_date=due_date, issued_by=issued_by)

            # 🔥 auto complete reservation
            Reservation.objects.filter(
                member=member, book=book, status="WAITING"
            ).update(status="COMPLETED")

            return Response({"message": "Book borrowed successfully"}, status=201)

        return Response(serializer.errors, status=422)


# Updated ReturnBookView
class ReturnBookView(GenericAPIView):

    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def post(self, request, pk):

        borrow = get_object_or_404(Borrow, id=pk)

        # ❌ already returned
        if borrow.is_returned:
            return Response({"message": "Book already returned"}, status=400)

        borrow.is_returned = True

        borrow.returned_at = timezone.now()

        today = date.today()

        # 💰 fine calculation
        if today > borrow.due_date:

            overdue_days = (today - borrow.due_date).days

            fine_per_day = 10

            borrow.fine_amount = overdue_days * fine_per_day

            # 🔔 overdue notification
            Notification.objects.create(
                member=borrow.member,
                title="Book Overdue",
                message=(f"You have been fined " f"{borrow.fine_amount}"),
                notification_type="OVERDUE",
            )

        else:
            borrow.fine_amount = 0

        borrow.save()

        # ⬆ restore stock
        book = borrow.book

        book.available_copies += 1

        book.save()

        # 🔥 reservation queue handling
        next_reservation = Reservation.objects.filter(
            book=book, status="WAITING"
        ).first()

        if next_reservation:

            next_reservation.notified = True
            next_reservation.save()

            # 🔔 reservation notification
            Notification.objects.create(
                member=next_reservation.member,
                title="Reserved Book Available",
                message=(f"{book.title} is now available."),
                notification_type="RESERVATION",
            )

        return Response(
            {"message": "Book returned successfully", "fine": borrow.fine_amount},
            status=200,
        )


# Updated OverdueBooksView
class OverdueBooksView(GenericAPIView):

    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def get(self, request):

        today = date.today()

        overdue_borrows = Borrow.objects.filter(is_returned=False, due_date__lt=today)

        result = []

        for borrow in overdue_borrows:

            overdue_days = (today - borrow.due_date).days

            fine_per_day = 10

            result.append(
                {
                    "member": borrow.member.full_name,
                    "book": borrow.book.title,
                    "due_date": borrow.due_date,
                    "overdue_days": overdue_days,
                    "current_fine": overdue_days * fine_per_day,
                }
            )

        return Response(result, status=200)
