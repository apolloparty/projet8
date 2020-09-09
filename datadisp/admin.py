from django.contrib import admin
from .models import Product_vanilla, Product_saved, User

# Register your models here.
admin.site.register(Product_vanilla)
admin.site.register(Product_saved)