from django.contrib import admin

from borrow.models import Borrow


# Register your models here.
@admin.register(Borrow)
class BorrowAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "member",
        "book",
        "issued_by",
        "issued_at",
        "due_date",
        "is_returned",
        "returned_at",
    )

    list_filter = (
        "is_returned",
        "issued_at",
        "due_date",
    )

    search_fields = (
        "member__full_name",
        "member__library_card_no",
        "book__title",
        "book__isbn",
        "issued_by__full_name",
    )

    list_editable = ("is_returned",)

    ordering = ("-issued_at",)
