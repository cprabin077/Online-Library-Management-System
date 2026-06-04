import uuid
from django.db import models


class Member(models.Model):

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

    address = models.TextField(blank=True, null=True)

    profile_image = models.ImageField(
        upload_to="member/profile/", null=True, blank=True
    )

    library_card_no = models.CharField(max_length=20, unique=True, blank=True)
    qr_code = models.CharField(max_length=100, unique=True, blank=True)

    is_active = models.BooleanField(default=False)

    joined_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        # 🧾 generate library card
        if not self.library_card_no:
            self.library_card_no = f"LIB-{uuid.uuid4().hex[:8].upper()}"

        # 📱 generate QR code data
        if not self.qr_code:
            self.qr_code = f"QR-{self.library_card_no}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
