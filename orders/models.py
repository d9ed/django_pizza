from django.db import models
from pizzas.models import Pizza


class Order(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('Processed', 'Processed'),
        ('Canceled', 'Canceled'),
        ('Delivered', 'Delivered'),
    ]
    pizza = models.ForeignKey(
        Pizza,
        on_delete=models.CASCADE,
        related_name='orders'
    )
    address = models.CharField(max_length=255, blank=None, null=None)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, null=False, blank=False, choices=STATUS_CHOICES,
                              default=STATUS_CHOICES[0][0])
    phone = models.CharField(max_length=50, null=False, blank=False)
    client_name = models.CharField(max_length=150, null=False, blank=False)
