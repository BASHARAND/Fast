from django.db import models
from django.forms import ModelForm
from django import forms
from django.forms.widgets import Widget
# Create your models here.
class Table(models.Model):
    table_num = models.CharField(primary_key=True,max_length=40)
    state=models.IntegerField(default=0)
    def __str__(self):
         return self.table_num

class Order(models.Model):
       table_num = models.ForeignKey(Table,on_delete=models.DO_NOTHING)
       date = models.DateField(auto_now_add=True)
       value=models.IntegerField(blank=True, null=True,default=0)
       state=models.IntegerField(default=0)
       lan= models.IntegerField(default=0)

       def __str__(self):
           return str(self.id)

class Category(models.Model):
    category = models.CharField(max_length=30)
    state=models.IntegerField(default=1)
    def __str__(self):
        return self.category

TITLE_CHOICES = (
    (1, 'FOOD'),
    (2, 'DRINKS'),
    (3, 'SWEETS'),
)
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=False)

    name = models.CharField(max_length=15)
    namear = models.CharField(max_length=15,blank=True,null=True)
    nameru = models.CharField(max_length=15,blank=True,null=True)
    description = models.TextField(max_length= 60)
    descriptionar = models.TextField(max_length=60,blank=True,null=True)
    descriptionru = models.TextField(max_length=60,blank=True,null=True)
    state = models.IntegerField(default=1)
    Price = models.IntegerField(default=15)
    Type = models.IntegerField(choices=TITLE_CHOICES)
    image = models.FileField(upload_to=' Profile_image', blank=True,null=True)

    def __str__(self):
        return self.name



class Get(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE , null=True)
    count= models.IntegerField(default=1)
    value = models.IntegerField(blank=True, null=True)
    state = models.IntegerField(default=0)
    def __str__(self):
        return str(self.id)

TITLE_Language = (
    (1, 'العربية'),
    (2, 'English'),
    (3, 'русский'),
    (4,'Türkçe')
)
class Rest(models.Model):
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    address=models.TextField(max_length=40)
    Language=models.IntegerField(choices=TITLE_Language)
    logo= models.FileField(upload_to=' Profile_image', blank=True,null=True)
    def __str__(self):
        return self.name

class accounts(models.Model):
    date = models.DateField(auto_now_add=True)
    value=models.IntegerField(default=0)
    def __str__(self):
        return self.category


