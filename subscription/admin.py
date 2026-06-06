from django.contrib import admin

from subscription.models import Subscription

# Register your models here.


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "plan_type",
        "price",
        "duration_days",
        "is_active",
        "created_at",
    )
    list_filter = ("plan_type", "is_active")
    search_fields = ("plan_type",)
    ordering = ("duration_days",)

    readonly_fields = ("created_at","duration_days","max_books", "max_borrow_days")
