from django.db import models


class Semla(models.Model):
    bakery = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='produkter/')
    vegan = models.BooleanField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    kind = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.bakery} - {self.city} - {self.kind} - {self.price} SEK"

