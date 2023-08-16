from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serilizers import UserRegestrationSerilizer,UserLoginSerilizer,UserProfileSerilizer,ChangePasswordSerilizer,SendPasswordResetEmailSerilizer,UserPasswordResetPasswordreset
from django.contrib.auth import login,authenticate
from .renderers import UserRenderer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Token generation
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def auth(request):
    return HttpResponse('auth Page')

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














        








