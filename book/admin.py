from django.contrib import admin

from book.models import Book

# Register your models here.


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "isbn",
        "publisher",
        "total_copies",
        "available_copies",
        "is_active",
        "published_date",
    )

    list_editable = (
        "total_copies",
        "available_copies",
        "is_active",
    )

    search_fields = (
        "title",
        "isbn",
        "authors__full_name",
        "categories__name",
        "publisher__name",
    )

    list_filter = (
        "is_active",
        "publisher",
        "categories",
        "authors",
        "published_date",
    )

    filter_horizontal = (
        "authors",
        "categories",
    )

    ordering = ("title",)
