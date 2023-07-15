from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
def auth(request):
    return HttpResponse('auth Page')

class UserRegestrationView(APIView):
    def post(self,request,format=None):
        return Response({'msg':"REgestration success"})