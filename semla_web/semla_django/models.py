from django.db import models


class Semla(models.Model):
    bakery = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='')
    vegan = models.BooleanField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    kind = models.CharField(max_length=50)

    def average_rating(self):
        return self.ratings.aggregate(models.Avg('score'))['score__avg'] or 0

    def __str__(self):
        return f"{self.bakery} - {self.city} - {self.kind} - {self.price} SEK"


class Rating(models.Model):
    semla = models.ForeignKey(
        Semla, related_name='ratings', on_delete=models.CASCADE)
    score = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True)
    ip_address = models.GenericIPAddressField()
    user_agent = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['ip_address', 'user_agent',
                        'semla', 'created_at__date'],
                name='unique_rating_per_day'
            )
        ]
