from django.db import models

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
    