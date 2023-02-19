from django import forms
from .models import Category

class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields =['category_name','description']
