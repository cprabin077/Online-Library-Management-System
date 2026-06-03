from django.contrib import admin

from category.models import Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "is_active",
        "created_at",
    )

    search_fields = ("name",)

    list_filter = (
        "is_active",
        "created_at",
    )

    ordering = ("name",)
