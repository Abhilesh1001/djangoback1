from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('newshonContact/',views.NewContactView.as_view()),
    path('prod/',views.ProductView.as_view()),
    path('singelprodview/<int:pk>',views.SingleProductView.as_view()),
    path('categorywiseview/',views.CategoryWiseView.as_view()),
    path('order/',views.NewOrder.as_view()),
    path('OrderUpdate/',views.OrderUpdateView.as_view()),
]
    