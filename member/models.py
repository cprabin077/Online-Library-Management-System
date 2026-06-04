import uuid
import qrcode
from io import BytesIO
from django.core.files import File
from django.db import models


class Member(models.Model):

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

    address = models.TextField(blank=True, null=True)

    profile_image = models.ImageField(upload_to="member/profile_image/", null=True, blank=True)

    library_card_no = models.CharField(max_length=20, unique=True, blank=True)

    qr_code = models.ImageField(upload_to="member/qr/", blank=True, null=True)

    is_active = models.BooleanField(default=True)

    joined_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        # Generate library card number
        if not self.library_card_no:
            self.library_card_no = str(uuid.uuid4()).split('-')[0].upper()

        super().save(*args, **kwargs)

        # Generate QR after saving (so ID exists)
        if not self.qr_code:
            qr = qrcode.make(self.library_card_no)

            buffer = BytesIO()
            qr.save(buffer, format='PNG')

            file_name = f"{self.library_card_no}.png"

            self.qr_code.save(file_name, File(buffer), save=False)

            super().save(update_fields=['qr_code'])

    def __str__(self):
        return self.full_name