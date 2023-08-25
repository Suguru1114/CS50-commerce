from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    first_name = models.TextField(max_length = 300)
    last_name = models.TextField(max_length = 300)

class Listing(models.Model):
    title = models.CharField(max_length=64, unique= True)
    text_description = models.CharField(max_length=255) 
    price = models.DecimalField(max_digits=10,decimal_places=2) 
    # 52;41
    def __str__(self):
        return f"{self.title}"
    # string reprisentatioin 

class Bids(models.Model):
    title = models.CharField(max_length=64, unique= True)
    price = models.DecimalField(max_digits=10,decimal_places=2) 

    def __str__(self):
        return f"{self.title}, {self.price}"




# class comments(models.Model):

# suguru pass
# suguru1114