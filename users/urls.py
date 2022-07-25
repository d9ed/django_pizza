from django.urls import path
from users.views import SignUpView, FeedBackView


urlpatterns = [
    path("register", SignUpView.as_view(), name="register"),
    path('feedback', FeedBackView.as_view(), name='feedback'),
]
