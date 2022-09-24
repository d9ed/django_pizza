import random
import os
from django.core.management.base import BaseCommand
from pizzas.models import Pizza


class Command(BaseCommand):
    help = 'Unalives all the pizzas in the shop'

    def handle(self, *args, **kwargs):
        Pizza.objects.all().delete()

    print("Pizzas are no more, rip")