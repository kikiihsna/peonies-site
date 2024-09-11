from django.db import models
import uuid

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    BOUQUET_TYPE_CHOICES = [
        ('single', 'Single'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('big', 'Big')
    ]

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    bouquet_type = models.CharField(max_length=10, choices=BOUQUET_TYPE_CHOICES, default='single')  # Type of bouquet
    wrap_color = models.CharField(max_length=50, default='')  # Wrap color

    def __str__(self):
        return self.name
    
    @property
    def is_in_stock(self):
        return self.stock > 0
