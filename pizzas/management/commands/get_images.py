import random
import os
from django.core.management.base import BaseCommand
from pizzas.models import Pizza
import json
from django_pizza import settings

class Command(BaseCommand):
    help = 'Unalives all the pizzas in the shop'

    def handle(self, *args, **kwargs):
        # print(Pizza.image.path())

        # with open(MEDIA_ROOT+"/", "r") as f:
        #     json.load(f)
        path = settings.MEDIA_ROOT
        img_list = os.listdir(path + '/pizza_images')
        context = {'images': img_list}
        print(context)