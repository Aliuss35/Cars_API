from rest_framework.decorators import api_view
#allows function to handle get post patch/put delete
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
from cars import serializers

#this is how we add decorators
@api_view(['GET'])
def cars_list(request):
  cars = Car.objects.all()

  serializer =CarSerializer(cars, many=True)

  return Response(serializer.data)#response from API to html. 

# Create your views here.
