from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import timedelta, date

from borrow.api.serializer import BorrowSerializer
from borrow.models import Borrow


# BORROW BOOK API
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

            #  MEMBER APPROVAL CHECK (FIXED)
            if not member.is_active:
                return Response(
                    {"error": "Member is not active (not approved)"},
                    status=403
                )

            #  LIMIT CHECK (MAX 3 BOOKS)
            active_count = Borrow.objects.filter(
                member=member,
                is_returned=False
            ).count()

            plan = member.subscription

            if not plan:
                return Response(
                    {"error": "No active subscription"},
                    status=400
                )

            if active_count >= plan.max_books:
                return Response(
                    {"error": "Borrow limit reached"},
                    status=400
                )

            #  STOCK CHECK
            if book.available_copies <= 0:
                return Response(
                    {"error": "Book not available"},
                    status=400
                )

            # ⬇ reduce stock
            book.available_copies -= 1
            book.save()

            #  due date
            due_date = timezone.now().date() + timedelta(
                days=plan.max_borrow_days
            )

            serializer.save(
                due_date=due_date,
                issued_by=issued_by
            )

            return Response(
                {"message": "Book borrowed successfully"},
                status=201
            )

        return Response(serializer.errors, status=422)

# RETURN BOOK API (WITH FINE)
class ReturnBookView(GenericAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer

    def post(self, request, pk):
        borrow = get_object_or_404(Borrow, id=pk)
        # already returned
        if borrow.is_returned:
            return Response({
                "message": "Book already returned"
                }, status=400)

        borrow.is_returned = True
        borrow.returned_at = timezone.now()
        today = date.today()

        # FINE CALCULATION
        if today > borrow.due_date:
            overdue_days = (today - borrow.due_date).days
            fine_per_day = 10
            borrow.fine_amount = overdue_days * fine_per_day
        else:
            borrow.fine_amount = 0
        borrow.save()

        # ⬆ restore stock
        book = borrow.book
        book.available_copies += 1
        book.save()

        return Response({
            "message": "Book returned successfully", "fine": borrow.fine_amount
            },status=200,)
    

# OVERDUE BOOKS API
class OverdueBooksView(GenericAPIView):
    queryset = Borrow.objects.all()
    serializer_class = BorrowSerializer


    def get(self, request):

        today = date.today()
        overdue_borrows = Borrow.objects.filter(is_returned=False,due_date__lt=today)
        result = []

        for borrow in overdue_borrows:
            overdue_days = (today - borrow.due_date).days
            fine_per_day = 10

            result.append({
                "member": borrow.member.full_name,
                "book": borrow.book.title,
                "due_date": borrow.due_date,
                "overdue_days": overdue_days,
                "current_fine": overdue_days * fine_per_day
            })

        return Response(result, status=200)
