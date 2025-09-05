from django.urls import path
from . import views

urlpatterns = [
    path("generate/", views.generate_itinerary, name="generate_itinerary"),
    path("", views.list_provinces, name="list_provinces"), 
    path("<int:province_id>/", views.get_province, name="get_province"), 
    path("<int:itinerary_id>/delete/", views.delete_itinerary, name="delete_itinerary"),
    path("preferences/", views.list_preferences, name="list_preferences"),
    path("transports/", views.list_transports, name="list_transports"),
]