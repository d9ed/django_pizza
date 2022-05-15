# from django.contrib import admin
from django.urls import path, include

from pizzas.views import PizzaListView, PizzaOrderView

urlpatterns = [
    path('', PizzaListView.as_view(), name='pizzas'),
    path('order/', PizzaOrderView.as_view(), name='order-pizza-form'),
]
