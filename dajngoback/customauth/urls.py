
from django.urls import path
from .import views


urlpatterns = [
    path('auth/', views.auth),
    path('authreg/',views.UserRegestrationView.as_view())
]
