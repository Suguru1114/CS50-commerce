from django.contrib import admin

from .models import User, Listing, Bid

# from django.contrib.auth.models import Listing, Bids 

# Register your models here.

# class ListingAdmin(admin.ModelAdmin):
    # list_display= ("title","text_description","price")

admin.site.register(User)
# admin.site.register(Category) 
admin.site.register(Listing)
admin.site.register(Bid)


# superuser; suguru
# password; 12345