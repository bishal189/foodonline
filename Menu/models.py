from django.db import models
from vendor.models import vendor

# Create your models here.

class Category(models.Model):
    vendor=models.ForeignKey(vendor,on_delete=models.CASCADE)
    category_name=models.CharField(max_length=50,unique=True)
    slug=models.SlugField(max_length=100,unique=True)
    description=models.TextField(max_length=250,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'

    def clean(self):
        self.category_name = self.category_name.capitalize()   
    
    def __str__(self):
        return self.category_name






class Fooditem(models.Model):
    vendor=models.ForeignKey(vendor,on_delete=models.CASCADE)
    Category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='fooditems')
    food_title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50,unique=True)
    descriptions=models.TextField(max_length=250,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='foodimages')
    is_availabe=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.food_title