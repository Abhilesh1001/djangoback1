from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from customauth.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serilizer import ContactSerilizer
from .models import Contact
from rest_framework import status

# Create your views here.
def shop(request):
    return HttpResponse('Shop page')



class ContactView(APIView):
    renderer_classes=[UserRenderer]
    # permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serilizer = ContactSerilizer(data=request.data)
        if serilizer.is_valid():
            contact = Contact(serilizer)
            contact.save()
            return Response({'msg':'Contact Saved SucessFully'})
        
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

