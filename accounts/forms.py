from django import forms
from .models import User
from .models import Userprofile
from .validation import  allow_only_images_validator



class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields=['first_name','last_name','username','email','password']
    
    
    def clean(self):
        cleaned_data= super(UserForm,self).clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        if password !=confirm_password:

            raise forms.ValidationError(
                'password does not match'
            )



class Userprofileform(forms.ModelForm):
    address=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter the addresss', 'required':'required'}))
    profile_picture=forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info'}),validators=[allow_only_images_validator ])
    cover_picture=forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info'}),validators=[allow_only_images_validator])
    # latitue=forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    # longitude=forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
   
   
    class Meta:
        model = Userprofile
        fields =['profile_picture','cover_picture','address','country','state','city','pin_code','latitue','longitude']

    def __init__(self,*args,**kwargs):
        super(Userprofileform,self).__init__(*args,**kwargs)
        for field in self.fields:
            if field == 'latitue' or field == 'longitude':
                self.fields[field].widget.attrs['readonly']='readonly'    