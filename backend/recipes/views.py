from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


from .models import Recipe, Ingredients, Procedure
from .serializers import *

@api_view(['GET', 'POST'])
def recipes_list(request):
    if request.method == 'GET':
        data = Recipe.objects.all()

        serializer = RecipeSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'PUT', 'DELETE'])
def recipe_details(request, pk):
    try:
        recipe = Recipe.objects.get(pk=pk)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = RecipeSerializer(recipe, context={'request': request})
        
        return Response(serializer.data)
    
    elif request.method == 'PUT':

        serializer = RecipeSerializer(recipe, data=request.data, context={'request': request})

        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

