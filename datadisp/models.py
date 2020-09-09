from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product_vanilla(models.Model):
    product = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=1)
    image_url = models.URLField()
    category = models.CharField(max_length=255, default="UNKNOW")
    energy = models.CharField(max_length=255, default="UNKNOW")
    energy_kcal = models.CharField(max_length=255, default="UNKNOW")
    fat = models.CharField(max_length=255, default="UNKNOW")
    saturated_fat = models.CharField(max_length=255, default="UNKNOW")
    carbohydrates = models.CharField(max_length=255, default="UNKNOW")
    sugar = models.CharField(max_length=255, default="UNKNOW")
    protein = models.CharField(max_length=255, default="UNKNOW")
    salt = models.CharField(max_length=255, default="UNKNOW")
    url = models.URLField(default="UNKNOW")
    def __str__(self):
        return self.product

class Product_saved(models.Model):
    product_requested = models.ForeignKey(Product_vanilla, on_delete=models.CASCADE, default="null")
    user = models.ForeignKey(User, on_delete=models.CASCADE)