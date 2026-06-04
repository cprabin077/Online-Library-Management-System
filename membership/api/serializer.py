from rest_framework import serializers

from membership.models import Membership


class MembershipSerializer(serializers.ModelSerializer):

    subscription_plan = serializers.CharField(
        source="subscription.get_plan_type_display", read_only=True
    )

    class Meta:
        model = Membership
        fields = [
            "id",
            "member",
            "subscription",
            "subscription_plan",
            "start_date",
            "end_date",
            "is_paid",
            "status",
            "created_at",
        ]

        read_only_fields = [
            "start_date",
            "end_date",
            "created_at",
        ]
