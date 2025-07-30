from django.db import models


class Restaurant(models.Model):
    name = models.CharField(max_length=64)
    address = models.CharField(max_length=128)
    rating = models.FloatField()

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField (max_length=64) 
    calories = models.SmallIntegerField() 
    is_vegetarian = models.BooleanField() 
    price = models.FloatField()

    def __str__(self):
        return f"{self.name} ({self.calories})"