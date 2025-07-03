from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['orderDate', 'requiredDate', 'status', 'customer']
        widgets = {
            'orderDate': forms.DateInput(attrs={'type': 'date'}),
            'requiredDate': forms.DateInput(attrs={'type': 'date'}),
        }