from django.contrib import admin

from librarian.models import Librarian

# Register your models here.from django.contrib import admin
@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'employee_id',
        'full_name',
        'email',
        'phone',
        'joining_date',
        'is_active',
    )

    list_editable = (
        'is_active',
    )

    search_fields = (
        'employee_id',
        'full_name',
        'email',
        'phone',
    )

    list_filter = (
        'is_active',
        'joining_date',
    )

    ordering = (
        'employee_id',
    )

    readonly_fields = (
        'employee_id',
        'created_at',
        'updated_at',
    )