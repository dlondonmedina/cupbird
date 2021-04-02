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
        fields = ['pk', 'name', 'description', 'ingredients', 'procedures']

    def create(self, validated_data):
        ingredients_data = validated_data.pop('ingredients')
        procedures_data = validated_data.pop('procedures')

        recipe = Recipe.objects.create(**validated_data)
        
        for ingredient in ingredients_data:
            Ingredients.objects.create(recipe=recipe, **ingredient)

        for proc in procedures_data:
            Procedure.objects.create(recipe=recipe, **proc)
        
        return recipe

    def update(self, instance, validated_data): 
        ingredients_data = validated_data.pop('ingredients')
        procedures_data = validated_data.pop('procedures') 

        ingredients = instance.ingredients.all()
        procedures = instance.procedures.all()
    
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)

        instance.save()

        for ingredient in ingredients:
            ing_data = next(i for i in ingredients_data if i['name'] == ingredient.name)
            ingredient.name = ing_data.get('name', ingredient.name)
            ingredient.qty = ing_data.get('qty', ingredient.qty)
            ingredient.unit = ing_data.get('unit', ingredient.unit)
            ingredient.save()

        for proc in procedures:
            proc_data = next(i for i in procedures_data if i['order'] == proc.order)
            proc.order = proc_data.get('order', proc.order)
            proc.process = proc_data.get('process', proc.process)
            proc.save()
        
        return instance 