from django.contrib.auth.models import AbstractUser, User
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
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True,null=True, related_name="category")
    image_url = models.URLField(blank=True, null=True)

    starting_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    current_highest_bid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    current_highest_bidder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    watchlist_users = models.ManyToManyField(User,related_name='watchlist_listings', blank=True)
    # isActive = models.BooleanField(default=True)
    # 52;41
    # def __str__(self):
    #     return f"{self.title}"
    # string reprisentatioin 
    is_closed  = models.BooleanField(default=False)

class Bid(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    timestamp = models.DateTimeField(auto_now_add=True)

# suguru pass
# suguru1114

class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listings = models.ManyToManyField('Listing')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)