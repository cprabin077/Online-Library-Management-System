from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)

    isbn = models.CharField(max_length=20, unique=True)

    authors = models.ManyToManyField("author.Author", related_name="books")
    categories = models.ManyToManyField("category.Category", related_name="books")

    publisher = models.ForeignKey(
        "publisher.Publisher",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="books",
    )

    published_date = models.DateField()

    total_copies = models.PositiveIntegerField(default=1)
    available_copies = models.PositiveIntegerField(default=1)

    description = models.TextField(blank=True, null=True)
    cover_image = models.ImageField(upload_to="books/", null=True, blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        db_table = "book"

    def __str__(self):
        return self.title
