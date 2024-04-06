from django.urls import path
from .views import PlaceApiView, PlaceDetailApiView, ReviewsApiView


app_name = 'api'

urlpatterns = [
    path('places-list/', PlaceApiView.as_view(), name="places"),
    path('place-detail/<int:id>/', PlaceDetailApiView.as_view(), name="place_detail"),


    path('reviews/', ReviewsApiView.as_view(), name="reviews"),

]