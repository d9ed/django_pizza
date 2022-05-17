from django.contrib import admin
from tabbed_admin import TabbedModelAdmin

from pizzas.models import Pizza, Topping


class ToppingInLine(admin.StackedInline):
    model = Pizza.toppings.through
    # filter_horizontal = ("toppings",)

# class ToppingInline(admin.TabularInline):
#     model = Topping
#     extra = 1


@admin.register(Topping)
class ToppingAdmin(TabbedModelAdmin):

    main_tab = (
        ('Main', {
            'fields': (
                'name',
                # 'pizza',
            )
        }),
    )

    tabs = [
        ('Main', main_tab),
    ]


@admin.register(Pizza)
class PizzaAdmin(TabbedModelAdmin):
    inlines = [ToppingInLine]

    main_tab = (
        ('Main', {
            'fields': (
                'name',
                'price',
                'size',
                'image',
            )
        }),
        ToppingInLine
    )

    tabs = [
        ('Main', main_tab),
    ]


