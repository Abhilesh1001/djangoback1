from django.urls import path
from .import views

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('auth/', views.auth),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('authreg/',views.UserRegestrationView.as_view()),
    path('authlogin/',views.UserLoginView.as_view()),
    path('authuserpro/',views.ProfileView.as_view()),
    path('changepassword/',views.UserChangePasswordView.as_view()),
    path('send-reset-password/',views.SendPasswordEmailView.as_view()),
    path('send-reset-password/<uid>/<token>/',views.UserPassewordResetView.as_view()),
    path('profile/<str:user>/', views.ProfileUpdateAPIView.as_view(), name='profile-detail'),
    path('profile/', views.UserProfileView.as_view(), name='profile-detail'),
]
