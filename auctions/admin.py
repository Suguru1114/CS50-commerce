from django.contrib import admin

from .models import User, Listing, Bid, Category

# from django.contrib.auth.models import Listing, Bids 

# Register your models here.

# class ListingAdmin(admin.ModelAdmin):
    # list_display= ("title","text_description","price")

admin.site.register(User)
# admin.site.register(Category) 
admin.site.register(Listing)
admin.site.register(Bid)
admin.site.register(Category)




# USERNAME
# superuser; suguru
# password; 12345

# test1
# test1