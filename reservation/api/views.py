from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from reservation.models import Reservation
from reservation.api.serializer import ReservationSerializer


class ReservationView(GenericAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get(self, request):
        reservations = Reservation.objects.all().order_by("-reserved_at")
        serializer = ReservationSerializer(reservations, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():
            member = serializer.validated_data["member"]
            book = serializer.validated_data["book"]

            # member approval check
            if not member.is_active:
                return Response({"error": "Member is not active"}, status=403)

            # reserve only unavailable books
            if book.available_copies > 0:
                return Response(
                    {"error": "Book is available. Borrow directly."}, status=400
                )

            # duplicate reservation check
            already_reserved = Reservation.objects.filter(
                member=member, book=book, status="WAITING"
            ).exists()

            if already_reserved:
                return Response({"error": "You already reserved this book"}, status=400)

            # OPTIONAL: reservation limit
            active_reservations = Reservation.objects.filter(
                member=member, status="WAITING"
            ).count()

            if active_reservations >= 5:
                return Response({"error": "Reservation limit reached (only 5 books can be reserved !!)"}, status=400)
            serializer.save()
            return Response({"message": "Book reserved successfully"}, status=201)
        return Response(serializer.errors, status=422)


class ReservationUpdateAndDelete(GenericAPIView):

    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def get(self, request, pk):
        reservation = get_object_or_404(Reservation, id=pk)
        serializer = ReservationSerializer(reservation)
        return Response(serializer.data, status=200)

    def delete(self, request, pk):
        reservation = get_object_or_404(Reservation, id=pk)
        reservation.status = "CANCELLED"
        reservation.save()
        return Response({"message": "Reservation cancelled successfully"}, status=200)
