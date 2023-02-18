from django import forms
from .models import vendor
from accounts.validation import  allow_only_images_validator

class VendorForm(forms.ModelForm):
    # for custom validation only filefild will work
    vendor_licences=forms.FileField(widget=forms.FileInput(attrs={'class':'btn btn-info'}),validators=[allow_only_images_validator])
    class Meta:
        model = vendor
        fields=['vendor_name','vendor_licences']
