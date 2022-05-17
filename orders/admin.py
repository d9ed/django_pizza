from django.contrib import admin
from tabbed_admin import TabbedModelAdmin

from orders.models import Order


@admin.register(Order)
class OrderAdmin(TabbedModelAdmin):

    readonly_fields = ('order_date',)

    main_tab = (
        ('Main', {
            'fields': (
                'pizza',
                'address',
                'order_date',
                'status',
                'phone',
                'client_name',
            )
        }),
    )

    tabs = [
        ('Main', main_tab),
    ]
