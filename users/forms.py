from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.forms import ModelForm
from django.contrib.auth import get_user_model


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name']
