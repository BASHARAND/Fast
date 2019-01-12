from django.contrib import admin

from django.contrib.auth.models import Group

from . models import Product, Order, Get,Table,Rest,Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'Price', 'Type')
    horizontal = ('namear',)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','table_num', 'date', 'value')

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Get)
admin.site.register(Category)
admin.site.register(Table)
admin.site.register(Rest)
admin.site.site_header='Restuarant Adminstration'
admin.site.site_title='SMART RESTURANT'