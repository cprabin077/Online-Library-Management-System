from rest_framework import serializers

from reservation.models import Reservation


class ReservationSerializer(serializers.ModelSerializer):
    member_name = serializers.CharField(source="member.full_name", read_only=True)
    book_title = serializers.CharField(source="book.title", read_only=True)

    class Meta:
        model = Reservation
        fields = [
            "id",
            "member",
            "member_name",
            "book",
            "book_title",
            "status",
            "notified",
            "reserved_at",
        ]

        read_only_fields = [
            "id",
            "status",
            "notified",
            "reserved_at",
        ]
