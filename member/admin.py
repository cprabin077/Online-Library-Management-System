from django.contrib import admin
from member.models import Member

# Register your models here.

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "full_name",
        "email",
        "phone",
        "library_card_no",
        "is_active",
        "joined_at",
    )

    readonly_fields = (
        "library_card_no",
        "qr_code",
        "is_active",
    )

    search_fields = (
        "full_name",
        "email",
        "phone",
        "library_card_no",
    )

    list_filter = (
        "is_active",
        "joined_at",
    )
