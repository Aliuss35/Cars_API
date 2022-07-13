from rest_framework.decorators import api_view
#allows function to handle get post patch/put delete
from rest_framework import status
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerializer


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
@api_view(['GET'])
def car_detail(request, pk):
 
  try:
    car = Car.objects.get(pk=pk)
    return Response(car)
  except Car.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  

# Create your views here.
