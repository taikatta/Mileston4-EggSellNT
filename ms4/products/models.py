from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    photo_main = models.ImageField(upload_to='photos/eggs')
    photo_1 = models.ImageField(upload_to='photos/eggs', blank=True)

    def __str__(self):
        return self.name