from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    # first_name = models.TextField(max_length = 300)
    # last_name = models.TextField(max_length = 300)
    pass

class Category(models.Model):
    categoryName = models.CharField(max_length=50)

class Listing(models.Model):
    title = models.CharField(max_length=64, unique= True)
    text_description = models.CharField(max_length=255) 
    price = models.FloatField()
    inActive = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, related_name="category")
    # isActive = models.BooleanField(default=True)
    # 52;41
    # def __str__(self):
    #     return f"{self.title}"
    # string reprisentatioin 

# class Bids(models.Model):
#     title = models.CharField(max_length=64, unique= True)
#     price = models.DecimalField(max_digits=10,decimal_places=2) 

    # def __str__(self):
    #     return f"{self.title}, {self.price}"
# use f dtring



# class comments(models.Model):

# suguru pass
# suguru1114