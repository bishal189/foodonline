from django import forms
from .models import Category
from .models import Fooditem
from accounts.forms import allow_only_images_validator

class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields =['category_name','description']



class Fooditemsform(forms.ModelForm):  
    image=forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info w-100'}),validators=[allow_only_images_validator ])
    class Meta:
        model = Fooditem
        fields =['Category','food_title','descriptions','price','image','is_availabe']
      
