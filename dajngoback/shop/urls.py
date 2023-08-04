from django.contrib import admin
from django.urls import path
from .import views


urlpatterns = [
    path('shop/', views.shop),
    path('shonContact/',views.ContactView.as_view())
]
