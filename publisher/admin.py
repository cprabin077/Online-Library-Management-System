from django.contrib import admin

from publisher.models import Publisher

# Register your models here.


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "name",
        "email",
        "phone",
        "website",
        "is_active",
        "created_at",
    )

    list_editable = ("is_active",)

    search_fields = (
        "name",
        "email",
        "phone",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    ordering = ("name",)
