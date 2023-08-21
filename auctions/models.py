from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):
    title = models.CharField(max_length=64, unique= True)
    text_description = models.CharField(max_digits=7,decimal_places=0) 
    price = models.DecimalField(max_digits=10,decimal_places=2) 

    def __str__(self):
        return self.titile 
    # string reprisentatioin 

# class bids(models.Model):

# class comments(models.Model):

# suguru pass
# suguru1114