from django.db import models

# Create your models here.


class Borrow(models.Model):

    member = models.ForeignKey(
        "member.Member", on_delete=models.CASCADE, related_name="borrows"
    )
    book = models.ForeignKey(
        "book.Book", on_delete=models.PROTECT, related_name="borrows"
    )
    issued_by = models.ForeignKey(
        "librarian.Librarian",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="issued_books",
    )
    issued_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    returned_at = models.DateTimeField(null=True, blank=True)
    fine_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    is_returned = models.BooleanField(default=False)
   
    class Meta:
        db_table = 'borrow'
        ordering = ["-issued_at"]

    def __str__(self):
        return f"{self.member.full_name} → {self.book.title}"
