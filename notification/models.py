from django.db import models

# Create your models here.

class Notification(models.Model):

    TYPE_CHOICES = (
        ('APPROVAL', 'Approval'),
        ('RESERVATION', 'Reservation'),
        ('DUE', 'Due Reminder'),
        ('OVERDUE', 'Overdue'),
    )

    member = models.ForeignKey(
        'member.Member',
        on_delete=models.CASCADE,
        related_name='notifications'
    )

    title = models.CharField(max_length=255)

    message = models.TextField()

    notification_type = models.CharField(
        max_length=20,
        choices=TYPE_CHOICES
    )

    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'notification'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
