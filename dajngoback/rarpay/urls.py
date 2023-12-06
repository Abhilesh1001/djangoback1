from django.urls import path
from .import views


urlpatterns = [
     path('order/create',views.index,name="create-order-api"),
]