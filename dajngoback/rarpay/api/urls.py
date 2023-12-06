from django.urls import path
from .razorpay_api import CreateOrderApiView,TranctionApiView


urlpatterns = [
     path('order/create',CreateOrderApiView.as_view(),name="create-order-api"),
     path('order/complete',TranctionApiView.as_view(),name="complete-order-api"),
]