from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from .customer import Customer


class Rating(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="ratings")
    score = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)],)

    class Meta:
        verbose_name = ("rating")
        verbose_name_plural = ("ratings")
