import random
from django.core.management.base import BaseCommand
from pizzas.models import Pizza, Topping, PizzaSize


class Command(BaseCommand):
    help = 'Populate pizzas'

    @staticmethod
    def _create_toppings_list():
        with open('pizzas/toppings.txt') as file:
            toppings_list = file.readlines()
            toppings_list = [topping.replace('\n', '') for topping in toppings_list]
        toppings_list = [Topping.objects.get_or_create(name=topping)[0] for topping in toppings_list]
        for topping in toppings_list:
            topping.save()
        return toppings_list

    @staticmethod
    def _read_pizza_names():
        with open('pizzas/pizza_names.txt') as file:
            pizza_names = file.readlines()
            pizza_names = [name.replace('\n', '') for name in pizza_names]
        return pizza_names

    def handle(self, *args, **kwargs):
        toppings_list = self._create_toppings_list()
        pizza_names = self._read_pizza_names()
        sizes_list = PizzaSize.objects.all()
        images_list = [pizza.image for pizza in Pizza.objects.all()]

        pizzas = [
            Pizza(
                name=name,
                image=random.choice(images_list),
                price=float(random.randint(100, 200))
            )
            for name in pizza_names
        ]

        Pizza.objects.bulk_create(pizzas)

        for pizza in pizzas:
            random_toppings = [random.choice(toppings_list) for _ in range(random.randint(5, 10))]
            pizza.toppings.add(*random_toppings)
            pizza.sizes.add(*sizes_list)
