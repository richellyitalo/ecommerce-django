from django import forms
from django_countries.fields import CountryField


PAYMENT_CHOICES = (
    ('PS', 'Pagseguro'),
    ('ML', 'Mercado Livre')
)


class CheckoutForm(forms.Form):
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Informe seu endereço'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Informe o seu apartamento'
    }))
    country = CountryField(blank_label='- Selecione um país -')
    zip = forms.CharField()
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect, choices=PAYMENT_CHOICES)
