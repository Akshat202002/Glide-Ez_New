from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("destination", views.destination_view, name="destination"),
    path("login_user", views.login_user_view, name="login_user"),
    path("register_user", views.register_user_view, name="register_user"),
    path("register_airline", views.register_airline_view, name="register_airline"),
    path("login_airline", views.login_airline_view, name="login_airline"),
    path("logout", views.logout_view, name="logout"),
    path("view_account", views.view_account_view, name="view_account"),
    path("pricing", views.pricing_view, name="pricing"),
    path("contact", views.contact_view, name="contact"),
    path("bookings", views.bookings_view, name="bookings"),
    path("search_flight", views.search_flight_view, name="search_flight")
    
]