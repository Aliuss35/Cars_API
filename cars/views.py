from rest_framework.decorators import api_view
#allows function to handle get post patch/put delete
from rest_framework.response import Response

#this is how we add decorators
@api_view(['GET'])
def cars_list(request):


  return Response('ok')#response from API to html. 

# Create your views here.
