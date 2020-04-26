from django.db import models


class Farm(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/farm')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
