from django.urls import path
from . import views

urlpatterns = [
    path('places/', views.places_list_api, name='places-list'),
    path('places/<int:place_id>/', views.place_detail_api, name='place_api'),
]