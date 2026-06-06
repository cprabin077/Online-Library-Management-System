from django.contrib import admin

from payment.models import Payment


# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "member",
        "subscription",
        "amount",
        "is_paid",
        "transaction_id",
        "paid_at",
        "created_at",
    ]

    list_filter = [
        "is_paid",
        "subscription",
    ]

    search_fields = [
        "member__full_name",
        "transaction_id",
    ]

    list_editable = [
        "is_paid",
    ]

    ordering = ["-created_at"]
