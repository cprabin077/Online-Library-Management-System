from django.db import models


class Librarian(models.Model):

    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(
        upload_to="librarian/profile/", null=True, blank=True
    )
    employee_id = models.CharField(max_length=20, unique=True, blank=True)
    joining_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "librarian"
        ordering = ["full_name"]

    def save(self, *args, **kwargs):

        # Auto-generate employee ID
        if not self.employee_id:
            last_librarian = Librarian.objects.order_by("id").last()
            if last_librarian:
                last_id = last_librarian.id + 1
            else:
                last_id = 1
            self.employee_id = f"LIB{last_id:03d}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.full_name} ({self.employee_id})"
