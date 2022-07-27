from tkinter import CASCADE

from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)  
    


class Product(models.Model):
    name  = models.CharField(max_length=100)
    price = models.IntegerField(max_length=7)
    stock = models.IntegerField(max_length=4)





