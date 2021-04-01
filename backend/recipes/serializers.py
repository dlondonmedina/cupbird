from rest_framework import serializers
from .models import Recipe, Ingredients, Procedure

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredients 
        fields = ['name', 'qty', 'unit']


class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Procedure
        fields = ['order', 'process']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    procedures = ProcedureSerializer(many=True)

    class Meta:
        model = Recipe 
        fields = ['name', 'description', 'ingredients', 'procedures']

