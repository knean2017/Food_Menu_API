from rest_framework.views import APIView, Response
from .serializers import RestaurantSerializer, FoodSerializer
from .models import Restaurant, Food


class RestaurantAPIView(APIView):
    def get(self, request):
        "Check all restaurants."
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    
class FoodAPIView(APIView):
    def get(self, request):
        "Check all food details."
        food_list = Food.objects.all()
        serializer = FoodSerializer(food_list, many=True)
        return Response(serializer.data)

class RestaurantDetailAPIView(APIView):
    def get(self, request, restaurant_id):
        "Check details of a specific restaurant."
        restaurant = Restaurant.objects.get(id=restaurant_id)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
    
class FoodDetailAPIView(APIView):
    def get(self, request, food_id):
        "Check details of a specific food item."
        food_item = Food.objects.get(id=food_id)
        serializer = FoodSerializer(food_item)
        return Response(serializer.data)
