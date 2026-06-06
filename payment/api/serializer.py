from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):

    member_name = serializers.CharField(source="member.full_name", read_only=True)

    subscription_name = serializers.CharField(
        source="subscription.get_plan_type_display", read_only=True
    )

    class Meta:

        model = Payment

        fields = [
            "id",
            "member",
            "member_name",
            "subscription",
            "subscription_name",
            "amount",
            "transaction_id",
            "is_paid",
            "paid_at",
            "created_at",
        ]

        read_only_fields = [
            "id",
            "transaction_id",
            "is_paid",
            "paid_at",
            "created_at",
        ]
