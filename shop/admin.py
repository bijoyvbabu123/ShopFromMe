from django.contrib import admin
from . import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'ref_id', 'total', 'status']




admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)