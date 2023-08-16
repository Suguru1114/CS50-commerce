from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64, unique= True)
    text_discription = models.CharField(max_digits=7,decimal_places=0) 
    price = models.DecimalField() 

    def __str__(self):
        return self.titile

# class bids(models.Model):

# class comments(models.Model):
