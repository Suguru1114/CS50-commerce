from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('create_listing/', views.create_listing, name='create_listing'),
    path('active_listing/', views.active_listing, name='active_listing'),
    path('add_to_watchlist/<int:listing_id>/', views.add_to_watchlist, name='add_to_watchlist'),
    path('watchlist/', views.watchlist, name='watchlist'),
    path('remove_from_watchlist/<int:item_id>/', views.remove_from_watchlist, name='remove_from_watchlist'),


    
]
