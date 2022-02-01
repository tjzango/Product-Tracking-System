from statistics import mode
from turtle import ondrag
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    serial_number = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    add_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.serial_number