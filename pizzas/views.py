from django.db.models import Sum, Q, Count
from django.shortcuts import render
from django.views.generic import ListView, View, DetailView
from django.http import HttpResponse, JsonResponse

from pizzas.models import Pizza, PizzaFilter
from pizzas.forms import PizzaOrderForm
from orders.models import Order


class PizzaListView(ListView):
    model = Pizza
    template_name = 'pizzas_list.html'
    context_object_name = 'pizzas'
    paginate_by = 12

    def get_queryset(self):
        q = super(PizzaListView, self).get_queryset().annotate(sizes_count=Count("sizes")).filter(
            Q(is_on_sale=True) &
            Q(sizes_count__gt=0)
        )

        pizza_filter = self.request.GET.get('filter', None)

        if pizza_filter is not None:
            q = q.filter(
                Q(filters=PizzaFilter.objects.filter(name=pizza_filter).first())
            )
        return q


    def get_context_data(self, *args, **kwargs):
        context = super(PizzaListView, self).get_context_data()
        context['filters'] = PizzaFilter.objects.all()

        return context


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
