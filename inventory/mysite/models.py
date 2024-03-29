from django.db import models
from django.utils import timezone
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),)
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveBigIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)
    qty = models.IntegerField()