from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)

    bio = models.TextField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "author"
        verbose_name = "Author"
        verbose_name_plural = "Authors"
        ordering = ['full_name']
        

    def __str__(self):
        return f'{self.full_name}'
