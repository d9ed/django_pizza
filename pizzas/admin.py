from django.contrib import admin
from tabbed_admin import TabbedModelAdmin

from pizzas.models import Pizza, Topping, PizzaSize, PizzaFilter


class ToppingInLine(admin.StackedInline):
    model = Pizza.toppings.through
    # filter_horizontal = ("toppings",)

# class ToppingInline(admin.TabularInline):
#     model = Topping
#     extra = 1


class PizzaSizeInline(admin.StackedInline):
    model = Pizza.sizes.through


class PizzaFilterInLine(admin.StackedInline):
    model = Pizza.filters.through


@admin.register(PizzaFilter)
class PizzaFilterAdmin(TabbedModelAdmin):
    main_tab = (
        ('Main', {
            'fields': (
                'name',
            )
        }),
    )

    tabs = [
        ('Main', main_tab),
    ]


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


@admin.register(PizzaSize)
class PizzaSizeAdmin(TabbedModelAdmin):

    main_tab = (
        ('Main', {
            'fields': (
                'size',
            )
        }),
    )

    tabs = [
        ('Main', main_tab),
    ]


@admin.register(Pizza)
class PizzaAdmin(TabbedModelAdmin):
    inlines = [ToppingInLine, PizzaSizeInline, PizzaFilterInLine]

    main_tab = (
        ('Main', {
            'fields': (
                'name',
                'price',
                # 'size',
                'image',
                'is_on_sale',
            )
        }),
        ToppingInLine,
        PizzaSizeInline,
        PizzaFilterInLine
    )

    tabs = [
        ('Main', main_tab),
    ]
