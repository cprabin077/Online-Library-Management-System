from django.contrib import admin

from membership.models import Membership


# Register your models here.
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "member",
        "subscription",
        "status",
        "is_paid",
        "start_date",
        "end_date",
        "created_at",
    )

    list_filter = (
        "status",
        "is_paid",
        "subscription",
    )

    search_fields = ("member__name",)

    ordering = ("-created_at",)

    readonly_fields = (
        "start_date",
        "end_date",
        "created_at",
    )
