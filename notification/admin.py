from django.contrib import admin

from notification.models import Notification

# Register your models here.


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "member",
        "notification_type",
        "title",
        "is_read",
        "created_at",
    ]

    list_filter = [
        "notification_type",
        "is_read",
    ]

    search_fields = [
        "member__full_name",
        "title",
    ]

    list_editable = [
        "is_read",
    ]

    ordering = ["-created_at"]
