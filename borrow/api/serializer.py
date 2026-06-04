from rest_framework import serializers

from borrow.models import Borrow


class BorrowSerializer(serializers.ModelSerializer):

    class Meta:
        model = Borrow

        fields = [
            "id",
            "member",
            "book",
            "issued_by",
            "issued_at",
            "due_date",
            "returned_at",
            "is_returned",
            "fine_amount",
        ]

        read_only_fields = [
            "issued_at",
            "due_date",
            "returned_at",
            "is_returned",
            "fine_amount",
        ]
