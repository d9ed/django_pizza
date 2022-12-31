from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import ListView, View, DetailView
from django.http import HttpResponse, JsonResponse

from pizzas.models import Pizza
from pizzas.forms import PizzaOrderForm
from orders.models import Order


class PizzaListView(ListView):
    model = Pizza
    template_name = 'pizzas_list.html'
    context_object_name = 'pizzas'
    paginate_by = 10

    def get_queryset(self):
        q = super(PizzaListView, self).get_queryset().filter(is_on_sale=True)
        return q


class PizzaDetailView(DetailView):
    model = Pizza
    template_name = "pizza_detail.html"


class PizzaOrderView(View):

    def post(self, request):

        form = PizzaOrderForm(request.POST)
        if form.is_valid():
            pizza_id = form.cleaned_data['pizza_id']
            pizza = Pizza.objects.filter(id=pizza_id)
            if pizza.exists():
                pizza = pizza.first()
                size = form.cleaned_data['size']
                if size in [s.size for s in pizza.sizes.all()]:
                    order = Order(
                        pizza=pizza,
                        address=form.cleaned_data['client_address'],
                        phone=form.cleaned_data['phone'],
                        client_name=form.cleaned_data['client_name'],
                        size=form.cleaned_data['size'],
                    )
                    order.save()
                    return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': dict(form.errors)})
