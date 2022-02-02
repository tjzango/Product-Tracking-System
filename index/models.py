from statistics import mode
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    serial_number = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    add_by = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.serial_number