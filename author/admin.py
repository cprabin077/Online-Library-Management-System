from django.contrib import admin

from author.models import Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "full_name",
        "email",
        "phone",
        "is_active",
        "created_at",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
    )

    list_filter = (
        "is_active",
        "created_at",
    )

    list_editable = (
        'is_active',
    )

    ordering = ("full_name",)
