from django.db import models


class Pizza(models.Model):
    SIZE_CHOICES = [
        ('24 cm', '24 cm'),
        ('32 cm', '32 cm'),
        ('40 cm', '40 cm'),
    ]
    name = models.CharField(max_length=255, null=False, blank=False)
    price = models.DecimalField(decimal_places=2, max_digits=4, null=False, blank=False)
    size = models.CharField(max_length=255, null=False, blank=False, choices=SIZE_CHOICES)


class Topping(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.CASCADE,
        related_name='toppings'
    )

    def __str__(self):
        return f"{self.name}"
