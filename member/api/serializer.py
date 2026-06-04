from rest_framework import serializers
from member.models import Member


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = [
            'id',
            'full_name',
            'email',
            'phone',
            'address',
            'profile_image',
            'library_card_no',
            'qr_code',
            'is_active',
            'joined_at',
        ]
        read_only_fields = [
            'id',
            'library_card_no',
            'qr_code',
            'is_active',
            'joined_at',
        ]

    def validate_email(self, value):
        member = self.instance  # 👈 important for update
        qs = Member.objects.filter(email=value)
        if member:
            qs = qs.exclude(id=member.id)
        if qs.exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_phone(self, value):
        member = self.instance
        qs = Member.objects.filter(phone=value)
        if member:
            qs = qs.exclude(id=member.id)
        if qs.exists():
            raise serializers.ValidationError("Phone already exists")
        return value