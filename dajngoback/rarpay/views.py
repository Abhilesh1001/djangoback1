from django.shortcuts import render,HttpResponse

# Create your views here.

from django.conf import settings

import razorpay

def index(request):
    client = razorpay.Client(auth=(
            settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET
        ))
    DATA = {
        "amount": 100,
        "currency": "INR",
        "receipt": "receipt#1",
        "notes": {
            "key1": "value3",
            "key2": "value2"
        }
    }

    # Use kwargs to pass the data to the create method
    order = client.order.create(data=DATA)

    # Verify the response or handle the order creation accordingly
    print(order) 
    return HttpResponse('ok')