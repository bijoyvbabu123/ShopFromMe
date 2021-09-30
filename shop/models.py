from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    AVAILABILITY = [
        ("YES", "yes"),
        ("NO", "no")
    ]

    name = models.CharField(max_length=100, verbose_name="Product Name", blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, verbose_name="Price")
    # the imagefield will save the images to the image_root in the settings since no path is specified. the default is also from the same path
    image = models.ImageField(default='placeholder.png', blank=False, verbose_name="Product Image")
    available = models.CharField(max_length=5, choices=AVAILABILITY, default=AVAILABILITY[0][1], blank=False, verbose_name="Available ?")

    def __str__(self):
        return self.name

    def get_all_available_products():
        return Product.objects.filter(available='YES').order_by('name')
        

class Order(models.Model):
    # first value is the value in the database and second one is the human-readable name
    ORDER_STATUS = [
        ("CART", "in cart"),
        ("PLACED", "order placed"),
        ("DONE", "completed")
    ]

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Customer")
    # to set the status accordingly... cart functionality is from this field... use get_or_create() for new cart or existing cart
    status = models.CharField(max_length=15, choices=ORDER_STATUS, default=ORDER_STATUS[0][1], blank=False, verbose_name="Status")
    # date is set to empty until the order is placed
    date = models.DateField(blank=True, null=True)
    # payment reference id for future use in case   .. the type of field is not yet sure, so setting it to a char field
    ref_id = models.CharField(max_length=100, blank=True, default="")
    # store the total amount only after placing the order
    total = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class OrderItems(models.Model):

    class Meta:
        verbose_name = "Order Items"
        verbose_name_plural = "Order Items"

    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name="order_id", blank=False)
    item = models.ForeignKey(Product, on_delete=models.CASCADE, blank=False) # set on_delete=RESTRICT or PROTECT after denying the permission to delete in Product model
    quantity = models.PositiveIntegerField()
    # rate of the product is stored after the order is placed
    rate = models.DecimalField(max_digits=10, decimal_places=2, blank=False, verbose_name="Rate")

    def __str__(self):
        return str(self.item)