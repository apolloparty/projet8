from django.db import models

# Create your models here.
class User(models.Model):
    """
    """
    name = models.CharField(max_length=58)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    """
    Create table and automate create two VARCHAR(30)
    and one TEXT()
    """
    product = models.CharField(max_length=200)
    brand = models.CharField(max_length=30)
    nutriscore = models.CharField(max_length=1)
    image_url = models.URLField()

    def __str__(self):
        """
        Permit to display selected author into django admin
        """
        return self.product


class Product_vanilla(models.Model):
    product = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    nutriscore = models.CharField(max_length=1)
    image_url = models.URLField()

    def __str__(self):
        return self.product

class Store(models.Model):
    store = models.CharField(max_length=100)
    random = models.ForeignKey(Product, on_delete=models.CASCADE)
    vanilla = models.ForeignKey(Product_vanilla, on_delete=models.CASCADE)
    def __str__(self):
        return self.store


class Product_saved(models.Model):
    product = models.CharField(max_length=200)
    brand = models.CharField(max_length=30)
    nutriscore = models.CharField(max_length=1)
    image_url = models.URLField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.product