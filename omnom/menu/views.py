from rest_framework.views import APIView, Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import get_object_or_404

from .serializers import RestaurantSerializer, FoodSerializer
from .models import Restaurant, Food


class RestaurantAPIView(APIView):
    def get(self, request):
        "Check all restaurants."
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=RestaurantSerializer)
    def post(self, request):
        data = request.data
        serializer = RestaurantSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Restaurant is ready!"})
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FoodAPIView(APIView):
    def get(self, request):
        "Check all food details."
        food_list = Food.objects.all()
        serializer = FoodSerializer(food_list, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=FoodSerializer)
    def post(self, request):
        data = request.data
        serializer = FoodSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({"Message": "Food is ready!"})
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RestaurantDetailAPIView(APIView):
    def get(self, request, restaurant_id):
        "Check details of a specific restaurant."
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
    
class FoodDetailAPIView(APIView):
    def get(self, request, food_id):
        "Check details of a specific food item."
        food_item = get_object_or_404(Food, id=food_id)
        serializer = FoodSerializer(food_item)
        return Response(serializer.data)
