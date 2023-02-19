from django import forms


class PaymentForm(forms.Form):
    tins = forms.CharField(max_length=200, min_length=32)  # на какие идентификационные номера налогоплательщиков будет начислена
    money = forms.DecimalField(max_digits=12, decimal_places=2)
