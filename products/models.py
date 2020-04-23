from django.db import models
from farm.models import Farm

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo_main = models.ImageField(upload_to='photos/eggs')
    farm = models.ForeignKey(Farm, on_delete=models.DO_NOTHING, default='', related_name='products')

    def __str__(self):
        return self.name