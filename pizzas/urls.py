# from django.contrib import admin
from django.urls import path, include

from pizzas.views import PizzaListView

urlpatterns = [
    path('', PizzaListView.as_view(), name='pizzas'),
]
