from django.contrib import admin
from . import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'available']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'date', 'ref_id', 'total', 'status']


class OrderItemsAdmin(admin.ModelAdmin):
    list_display = ['order', 'item', 'quantity', 'rate']




admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Order, OrderAdmin)
admin.site.register(models.OrderItems, OrderItemsAdmin)