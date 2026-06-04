from rest_framework import serializers
from librarian.models import Librarian


class LibrarianSerializer(serializers.ModelSerializer):

    class Meta:
        model = Librarian

        fields = [
            "id",
            "full_name",
            "email",
            "phone",
            "address",
            "profile_image",
            "employee_id",
            "joining_date",
            "is_active",
            "created_at",
            "updated_at",
        ]

        read_only_fields = [
            "id",
            "employee_id",
            "created_at",
            "updated_at",
        ]

    def validate_email(self, value):
        librarian = self.instance
        qs = Librarian.objects.filter(email=value)
        if librarian:
            qs = qs.exclude(id=librarian.id)
        if qs.exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_phone(self, value):
        librarian = self.instance
        qs = Librarian.objects.filter(phone=value)
        if librarian:
            qs = qs.exclude(id=librarian.id)
        if qs.exists():
            raise serializers.ValidationError("Phone already exists")
        return value
