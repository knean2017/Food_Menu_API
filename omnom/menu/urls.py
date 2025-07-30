from django.urls import path, include
from .views import RestaurantAPIView, FoodAPIView, RestaurantDetailAPIView, FoodDetailAPIView


urlpatterns = [
    path("restaurant/", RestaurantAPIView.as_view(), name="Restaurant"),
    path("food/", FoodAPIView.as_view(), name="Food"),

    path("restaurant/<int:restaurant_id>/",RestaurantDetailAPIView.as_view(), name="RestaurantDetail"),
    path("food/<int:food_id>/", FoodDetailAPIView.as_view(), name="FoodDetail"),
]
