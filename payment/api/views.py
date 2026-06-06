from datetime import timedelta

from django.shortcuts import get_object_or_404
from django.utils import timezone

from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from payment.models import Payment


class ConfirmPaymentView(GenericAPIView):

    def post(self, request, pk):

        payment = get_object_or_404(Payment, id=pk)

        # ❌ already paid
        if payment.is_paid:
            return Response({"error": "Payment already completed"}, status=400)

        # ✅ payment success
        payment.is_paid = True

        payment.transaction_id = f"TXN-{payment.id}"

        payment.paid_at = timezone.now()

        payment.save()

        # 🔥 ACTIVATE MEMBER SUBSCRIPTION
        member = payment.member
        plan = payment.subscription

        today = timezone.now().date()

        member.subscription = plan

        member.subscription_start = today

        member.subscription_end = today + timedelta(days=plan.duration_days)

        member.save()

        return Response(
            {
                "message": "Payment successful",
                "plan": plan.get_plan_type_display(),
                "subscription_end": member.subscription_end,
            },
            status=200,
        )
