from customerapp.models import Customer
from django import forms

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
