from django.db import models

# Create your models here.
STATUS_CHOICES = (
    ("WAITING", "Waiting"),
    ("COMPLETED", "Completed"),
    ("CANCELLED", "Cancelled"),
)


class Reservation(models.Model):

    member = models.ForeignKey(
        "member.Member", on_delete=models.CASCADE, related_name="reservations"
    )

    book = models.ForeignKey(
        "book.Book", on_delete=models.CASCADE, related_name="reservations"
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="WAITING")

    notified = models.BooleanField(default=False)

    reserved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reservation"
        ordering = ["reserved_at"]

        # constraints = [
        #     models.UniqueConstraint(
        #         fields=["member", "book"],
        #         condition=models.Q(status="WAITING"),
        #         name="unique_active_reservation",
        #     )
        # ]

    def __str__(self):
        return f"{self.member.full_name} reserved {self.book.title}"
