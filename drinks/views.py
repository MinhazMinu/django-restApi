from django.http import JsonResponse
from .serializers import DrinkSerializer
from .models import Drink


def drink_request(request):
    # ge all the drinks
    drinks = Drink.objects.all()
    # serialize them
    serializer = DrinkSerializer(drinks, many=True)
    # return the serialized data
    return JsonResponse({"drinks": serializer.data}, safe=False)
