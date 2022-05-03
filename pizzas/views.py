from django.shortcuts import render
from django.views.generic import ListView

from pizzas.models import Pizza


class PizzaListView(ListView):
    model = Pizza
    template_name = 'pizzas_list.html'
    context_object_name = 'pizzas'
