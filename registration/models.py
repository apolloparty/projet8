from django.db import models


# Create your models here.

# CUSTOM METHOD USER
class User(models.Model):
    """
    """
    username = models.CharField(max_length=58)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255, default="")

    def __str__(self):
        return self.username

