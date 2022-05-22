from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from users.forms import UserRegisterForm


class SignUpView(CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('pizzas')
    form_class = UserRegisterForm
