from django import forms
from .models import Shop
from django.forms import ModelForm, TextInput, Select

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['category','name','location','image','delivery','description',]
        # fields = '__all__'
        widgets = {
            'name' : TextInput(attrs={
                'style': 'max_width:200px;',
                'placeholder': 'Enter name of shop'
            }),
        }