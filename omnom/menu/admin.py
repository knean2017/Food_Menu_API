from django.contrib import admin
from .models import Restaurant, Food

@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'rating')
    search_fields = ('name', 'address')
    list_filter = ('rating',)
    ordering = ('-rating',)

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories', 'is_vegetarian', 'price')
    search_fields = ('name',)
    list_editable = ('price',)
    ordering = ('name',)
