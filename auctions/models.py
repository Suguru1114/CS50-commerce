from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class listing(models.Model):
    title = models.CharField(max_length=64, unique= True)
    text_discription = models.CharField(max_digits=7,decimal_places=0) 
    price = models.DecimalField() 

# class bids(models.Model):

# class comments(models.Model):
