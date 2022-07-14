from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
#allows function to handle get post patch/put delete
from rest_framework import status
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer
from cars import serializers


#this is how we add decorators
@api_view(['GET', 'POST'])
def cars_list(request):

  if request.method == 'GET':
    cars = Car.objects.all()
    serializer =CarSerializer(cars, many=True)
    return Response(serializer.data)
  elif request.method == 'POST':
    serializer =CarSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
   

  # return Response(serializer.data)#response from API to html. 
@api_view(['GET','PUT', 'DELETE'])
def car_detail(request, pk):
  car = get_object_or_404(Car, pk=pk)
  if request.method == 'GET':
    serializer=CarSerializer(car)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer=CarSerializer(car, data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)
  elif request.method == 'DELETE':
    car.delete()
    return Response(status=status.HTTP_204_NO_CONTENT_)
    
  

# Create your views here.
