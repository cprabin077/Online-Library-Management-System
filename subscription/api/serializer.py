from rest_framework import serializers
from subscription.models import Subscription


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            "id",
            "plan_type",
            "price",
            "duration_days",
            "is_active",
            "created_at",
        ]
        
        read_only_fields = ["duration_days", "created_at"]
