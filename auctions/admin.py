from django.contrib import admin

from .models import Listing, Bids

# Register your models here.

class ListingAdmin(admin.ModelAdmin):
    list_display= ("title","text_description","price")

admin.site.register(Listing, ListingAdmin) 
admin.site.register(Bids)