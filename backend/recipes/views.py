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
        return "Not built yet"

