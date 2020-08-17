from django.db import models

# Create your models here.
# Pickup @ the Activating Models Section Of Tutorial
from django.db import models

class Business(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    email = models.EmailField
    logo = models.ImageField



class FeatureProduct(models.Model):
    belongsTo = models.ForeignKey(Business, blank=True, null=True, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    shipping_time = models.CharField(max_length=200)
    price = models.DecimalField
    product_image = models.ImageField
    product_link = models.CharField(max_length=200)
