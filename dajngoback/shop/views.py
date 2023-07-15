from django.shortcuts import render,HttpResponse

# Create your views here.
def shop(request):
    return HttpResponse('Shop page')