from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=150, unique=True)

    email = models.EmailField(unique=True, blank=True, null=True)
    phone = models.CharField(max_length=20, unique=True, blank=True, null=True)

    address = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Publisher"
        verbose_name_plural = "Publishers"
        ordering = ['name']

    def __str__(self):
        return self.name
