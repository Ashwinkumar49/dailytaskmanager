from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    phone = models.IntegerField(max_length=10)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
