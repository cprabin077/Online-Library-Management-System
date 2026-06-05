from django.contrib import admin

from reservation.models import Reservation


# Register your models here.
@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "member",
        "book",
        "status",
        "notified",
        "reserved_at",
    ]

    list_filter = [
        "status",
        "notified",
    ]

    search_fields = [
        "member__full_name",
        "book__title",
    ]

    list_editable = [
        "status",
        "notified",
    ]

    ordering = ["-reserved_at"]
