from django.shortcuts import render
from django.views.generic import ListView, View
from django.http import HttpResponse, JsonResponse

from pizzas.models import Pizza
from pizzas.forms import PizzaOrderForm
from orders.models import Order

class PizzaListView(ListView):
    model = Pizza
    template_name = 'pizzas_list.html'
    context_object_name = 'pizzas'


class PizzaOrderView(View):
    def post(self, request):
        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            pizza_id = form.cleaned_data['pizza_id']
            pizza = Pizza.objects.filter(id=pizza_id)
            if pizza.exists():
                pizza = pizza.first()
                order = Order(
                    pizza=pizza,
                    address=form.cleaned_data['client_address'],
                    phone=form.cleaned_data['phone'],
                    client_name=form.cleaned_data['client_name'],
                )
                order.save()
                print(f'order:{order}')
                return JsonResponse({'success': True})
        return JsonResponse({'success': False})

