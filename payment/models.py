from django.db import models

# Create your models here.


class Payment(models.Model):
    member = models.ForeignKey(
        "member.Member", on_delete=models.CASCADE, related_name="payments"
    )
    subscription = models.ForeignKey(
        "subscription.Subscription", on_delete=models.CASCADE
    )
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    paid_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'payment'

    def __str__(self):
        return f"{self.member.full_name} - {self.amount}"
