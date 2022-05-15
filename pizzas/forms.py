from django import forms
from django.core.exceptions import ValidationError


class PizzaOrderForm(forms.Form):
    pizza_id = forms.CharField()
    phone = forms.CharField(max_length=50)
    client_name = forms.CharField(max_length=150)
    client_address = forms.CharField(max_length=200)

    def clean(self):
        super().clean()
        try:
            pizza_id = int(self.cleaned_data.get("pizza_id"))
        except ValueError:
            raise ValidationError('pizza_id not int')
        phone = self.cleaned_data.get("phone")
        client_name = self.cleaned_data.get("client_name")
        client_address = self.cleaned_data.get("client_address")
        if phone == "" or client_address == "" or client_name == "":
            raise ValidationError('some fields are empty')
        if not isinstance(pizza_id, int):
            raise ValidationError('pizza_id not int')
