from dataclasses import fields
from rest_framework import serializers
from Drinks.models import Drink

class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id', 'drink_name', 'drink_description']
