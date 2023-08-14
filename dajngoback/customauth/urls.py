
from django.urls import path
from .import views



urlpatterns = [
    path('auth/', views.auth),
    path('authreg/',views.UserRegestrationView.as_view()),
    path('authlogin/',views.UserLoginView.as_view()),
    path('authuserpro/',views.ProfileView.as_view()),
    path('changepassword/',views.UserChangePasswordView.as_view()),
    path('send-reset-password/',views.SendPasswordEmailView.as_view()),
    path('send-reset-password/<uid>/<token>/',views.UserPassewordResetView.as_view()),
]
