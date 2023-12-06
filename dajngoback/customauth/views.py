from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serilizers import UserRegestrationSerilizer,UserLoginSerilizer,UserProfileSerilizer,ChangePasswordSerilizer,SendPasswordResetEmailSerilizer,UserPasswordResetPasswordreset,UserProfileSErilizer,ProfileUpdateSerializer,UserProfileSerializer
from django.contrib.auth import login,authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .models import ProfileUpdate
from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework.decorators import api_view

# Create your views here.

# Token generation

class TokenRefreshAPIView(TokenRefreshView):
    pass 

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    access_token = str(refresh.access_token)
    refresh_token = str(refresh)

    return {
        'refresh':  refresh_token,
        'access': access_token,
    }




def auth(request):
    return HttpResponse('auth Page')






@api_view(['POST'])  # Decorator to define the view for handling requests
def refresh_access_token(request):
    refresh_token = request.data.get('refresh_token')  # Assuming you receive the refresh token in the request data

    if refresh_token:
        new_access_token = get_access_token_from_refresh_token(refresh_token)
        if new_access_token:
            return Response({'new_access_token': new_access_token}, status=status.HTTP_200_OK)
    
    return Response({'error': 'Failed to refresh access token'}, status=status.HTTP_400_BAD_REQUEST)

def get_access_token_from_refresh_token(refresh_token):
    try:
        refresh = RefreshToken(refresh_token)
        access_token = str(refresh.access_token)
        return access_token
    except Exception as e:
        # Handle token refresh failure or invalid token
        return None



class UserRegestrationView(APIView):
    renderer_classes=[UserRenderer]
    
    def post(self,request,format=None):
        serilizer = UserRegestrationSerilizer(data=request.data) 
        # print(serilizer)  
        if serilizer.is_valid(raise_exception=True):
            user =serilizer.save()  
            token=get_tokens_for_user(user)
            return Response({'token':token,'msg':"Regestration success"},status=status.HTTP_201_CREATED)

        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serilizers = UserLoginSerilizer(data=request.data)
        print(serilizers)
        if serilizers.is_valid(raise_exception=True):
            email = serilizers.data.get('email')
            password = serilizers.data.get('password')
            user=authenticate(email=email,password=password)
            token=get_tokens_for_user(user)
            if user is not None:
                return Response({'token':token,'msg':'Login Successs'},status=status.HTTP_200_OK)
            else: 
                return Response({'errors':{'non_fields_errors':['Email or password is not valid']}},status=status.HTTP_400_BAD_REQUEST)
        return Response(serilizers.errors,status=status.HTTP_400_BAD_REQUEST)
    

class ProfileView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        serilzer = UserProfileSerilizer(request.user)
        return Response(serilzer.data,status=status.HTTP_200_OK)
    


class UserChangePasswordView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serilizer = ChangePasswordSerilizer(data=request.data,context = {'user':request.user})
        if serilizer.is_valid(raise_exception=True):
            return Response({'msg':'Password changed successufully'},status=status.HTTP_200_OK)

        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    
class SendPasswordEmailView(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serilizer = SendPasswordResetEmailSerilizer(data=request.data)
        if serilizer.is_valid(raise_exception=True):
            return Response({'msg':'Password Reset link senf Please check your Email'},status=status.HTTP_200_OK)
        
        return Response(serilizer.errors,status=status.HTTP_400)



class UserPassewordResetView(APIView):
    renderer_classes = [UserRenderer]
    def post(self,request,uid,token,format=None):
        print('uidhome',uid)
        serilizers = UserPasswordResetPasswordreset(data=request.data,context ={'uid':uid,'token':token})
        if serilizers.is_valid(raise_exception=True):
            return Response({'msg':'Pasword Reset Sucefully'},status=status.HTTP_200_OK)
        return Response(serilizers.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserProfileView(APIView):
    renderer_classes = [UserRenderer] 

    def get(self, request, format=None):
        profiles = ProfileUpdate.objects.all()
        serializer = UserProfileSerializer(profiles, many=True) 
        return Response(serializer.data)



class ProfileUpdateAPIView(APIView):
    def get_object(self, user):
        try:
            return ProfileUpdate.objects.get(user=user)
        except ProfileUpdate.DoesNotExist:
            return None

    def get(self, request, user):
        profile = self.get_object(user)
        if profile:
            serializer = ProfileUpdateSerializer(profile)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = ProfileUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, user):
        profile = self.get_object(user)
        if profile:
            serializer = ProfileUpdateSerializer(profile, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, user):
        profile = self.get_object(user)
        if profile:
            serializer = ProfileUpdateSerializer(profile, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)










        








