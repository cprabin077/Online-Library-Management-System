from rest_framework import serializers

from notification.models import Notification


class NotificationSerializer(serializers.ModelSerializer):

    member_name = serializers.CharField(source="member.full_name", read_only=True)
    class Meta:
        model = Notification
        fields = [
            "id",
            "member",
            "member_name",
            "title",
            "message",
            "notification_type",
            "is_read",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "created_at",
        ]
