from django.db import models


class Subscription(models.Model):

    class PlanType(models.TextChoices):
        MONTHLY = "1m", "1 Month"
        THREE_MONTHS = "3m", "3 Months"
        SIX_MONTHS = "6m", "6 Months"
        TWELVE_MONTHS = "12m", "12 Months"

    plan_type = models.CharField(
        max_length=10,
        choices=PlanType.choices,
        unique=True
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    duration_days = models.PositiveIntegerField(
        blank=True,
        null=True
    )

    # 🔥 LMS Rules
    max_books = models.PositiveIntegerField(default=3)

    max_borrow_days = models.PositiveIntegerField(default=7)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        mapping = {
            "1m": 30,
            "3m": 90,
            "6m": 180,
            "12m": 365,
        }

        if self.plan_type in mapping:
            self.duration_days = mapping[self.plan_type]

        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_plan_type_display()

    class Meta:
        db_table = "subscription"
        ordering = ["duration_days"]