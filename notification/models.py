from django.db import models

# Create your models here.
NOTIFICATION_TYPES = (
    ("approval", "Approval"),
    ("reservation", "Reservation"),
    ("due_reminder", "Due Reminder"),
    ("overdue", "Overdue"),

    ("new_book", "New Book Added"),
    ("announcement", "Announcement"),
    ("fine", "Fine Applied"),

    ("payment_success", "Payment Success"),
    ("payment_failed", "Payment Failed"),
)


class Notification(models.Model):

    member = models.ForeignKey(
        "member.Member", on_delete=models.CASCADE, related_name="notifications"
    )

    title = models.CharField(max_length=255)

    message = models.TextField()

    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPES)

    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notification"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
