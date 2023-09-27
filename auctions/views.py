from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ListingForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import User, Listing, Category, Bid, Watchlist


def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


    # add new listin gfunction here to able user to addd new listing 



def active_listing(request):
    listings = Listing.objects.all()
    return render(request, "auctions/active_listing.html", {'listings': listings})


def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            new_listing = form.save(commit=False)
            new_listing.owner = request.user
            # Assign the current user as the owner
            new_listing.save()
            return redirect('index')
        # Redirect to the homepage or another page

    else: 
        form = ListingForm()

    return render(request, 'auctions/create_listing.html', {
        'form':form
     })

def add_to_watchlist(request, listing_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to add items to your watchlist.")
        return redirect('login')  # Redirect to the login page or any other appropriate page

    listing = get_object_or_404(Listing, pk=listing_id)

    user_watchlist, created = Watchlist.objects.get_or_create(user=request.user)
    user_watchlist.listings.add(listing)
    
    return redirect('watchlist')

def watchlist(request):
    if request.user.is_authenticated:
        # Retrieve the user's watchlist items here, assuming you have a Watchlist model
        user_watchlist = Watchlist.objects.get(user=request.user)
        watchlist_items = user_watchlist.listings.all()
    else:
        watchlist_items = []  # Empty list if the user is not authenticated

    return render(request, "auctions/watchlist.html", {'watchlist_items': watchlist_items})

def remove_from_watchlist(request, item_id):
    item = get_object_or_404(Listing, pk=item_id)
    
    if request.user.is_authenticated:
        user_watchlist = Watchlist.objects.get(user=request.user)
        user_watchlist.listings.remove(item)
    
    return redirect('watchlist')
