from django import forms
from .models import Listing, Category, Bid


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['title', 'text_description', 'price', 'image_url', 'category']


        # i might need bids here 
