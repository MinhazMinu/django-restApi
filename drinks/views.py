from .serializers import DrinkSerializer
from .models import Drink
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(["GET", "POST"])
def drink_request(request, format=None):
    if request.method == "GET":
        # ge all the drinks
        drinks = Drink.objects.all()
        # serialize them
        serializer = DrinkSerializer(drinks, many=True)
        # return the serialized data
        return Response(serializer.data)
    if request.method == "POST":
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def drink_detail(request, id, format=None):
    if request.method == "GET":
        try:
            drink = Drink.objects.get(id=id)
        except Drink.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    elif request.method == "PUT":
        drink = Drink.objects.get(id=id)
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    elif request.method == "DELETE":
        drink = Drink.objects.get(id=id)
        drink.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
