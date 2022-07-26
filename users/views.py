from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView

from users.forms import UserRegisterForm
from users.models import FeedbackRequest


class SignUpView(CreateView):
    template_name = 'registration/register.html'
    success_url = reverse_lazy('pizzas')
    form_class = UserRegisterForm


class FeedBackView(CreateView):
    model = FeedbackRequest
    template_name = "feedback_page.html"
    fields = ['name', 'email', 'subject', 'message']
    success_url = reverse_lazy('pizzas')
