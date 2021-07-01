from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=30)
    user =models.CharField(max_length=60)
    password =models.CharField(max_length=20)

class Moderadores(models.Model):
    
    email = models.EmailField(max_length=30)
    moduser =models.CharField(max_length=60)
    password =models.CharField(max_length=20)
