from django.db import models
from datetime import date, timedelta


class Membership(models.Model):

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        ACTIVE = "active", "Active"
        EXPIRED = "expired", "Expired"
    member = models.ForeignKey(
        "member.Member",
        on_delete=models.CASCADE,
        related_name="memberships",
    )
    subscription = models.ForeignKey(
        "subscription.Subscription",
        on_delete=models.CASCADE,
        related_name="memberships",
    )
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.PENDING,
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def activate_membership(self):
        self.is_paid = True
        self.status = self.Status.ACTIVE
        self.start_date = date.today()
        self.end_date = self.start_date + timedelta(
            days=self.subscription.duration_days
        )

        self.save()

    def __str__(self):
        return f"{self.member}"