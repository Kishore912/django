from django import forms
from .models import product



class ProductForm(forms.ModelForm):
    class meta:
        model=product
        field=[
            'title',
            'description',
            'price'
        ]