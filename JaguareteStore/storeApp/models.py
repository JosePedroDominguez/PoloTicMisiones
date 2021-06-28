from django.db import models

# Create your models here.
class Items(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='productos')
    tag  = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.FloatField()

class User(models.Model):
    email = models.EmailField(max_length=30)
    user =models.CharField(max_length=60)
    password =models.CharField(max_length=20)

class Moderadores(models.Model):
    email = models.EmailField(max_length=30)
    moduser =models.CharField(max_length=60)
    password =models.CharField(max_length=20)
