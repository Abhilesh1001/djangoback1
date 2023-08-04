
from django.urls import path
from .import views



urlpatterns = [
    path('auth/', views.auth),
    path('authreg/',views.UserRegestrationView.as_view()),
    path('authlogin/',views.UserLoginView.as_view()),
    path('authuserpro/',views.ProfileView.as_view())
]
