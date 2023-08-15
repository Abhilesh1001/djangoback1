from rest_framework import serializers
from customauth.models import User
from django.utils.encoding import smart_str, force_bytes,DjangoUnicodeDecodeError
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode

class UserRegestrationSerilizer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields = ['email','name','password','password2','tc']
        extra_kwargs = {
            'password':{'write_only':True}
        }
    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        # print(password,password2)
        if(password !=password2):
            raise serializers.ValidationError('Password and confirm password doesnot matched')
        return attrs
    
    def create(self,validata_data):
        return User.objects.create_user(**validata_data)


class UserLoginSerilizer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=255)
    class Meta:
     model = User
     fields = ["id",'email', 'password']

class UserProfileSerilizer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','email','name']


class ChangePasswordSerilizer(serializers.Serializer):
    password = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True) 
    password2 = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True) 
    class Meta:
        fields = ['password','password2']
    
    def validate(self, attrs):
        password =attrs.get('password')
        password2 = attrs.get('password2')
        user = self.context.get('user')
        if password !=password2:
            raise serializers.ValidationError('password and confirm password doesnot matched')

        user.set_password(password)
        user.save()
        return attrs
    

class SendPasswordResetEmailSerilizer(serializers.Serializer):
    email = serializers.EmailField(max_length=245)
    class Meta:
        fields = ['email']
    
    def validate(self, attrs):
        email = attrs.get('email')
        print(email)
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uid = urlsafe_base64_encode(force_bytes(user.id))
            token =PasswordResetTokenGenerator().make_token(user)
            link = 'http://127.0.0.1:5173/auth/resetpassworduidtoken/'+uid+'/'+token
            print('password Reset link',link)
            return attrs
        else:
            raise serializers.ValidationError('You are not a Register User')


class UserPasswordResetPasswordreset(serializers.Serializer):
    password = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True) 
    password2 = serializers.CharField(max_length=255,style={'input_type':'password'},write_only=True) 
    class Meta:
        fields = ['password','password2']
    
    def validate(self, attrs):
        try :
            password =attrs.get('password')
            password2 = attrs.get('password2')
            uid =self.context.get('uid')
            token = self.context.get('token')
            print('uid',uid,'token',token)
            if password !=password2:
                raise serializers.ValidationError('password and confirm password doesnot matched')
            
            id = smart_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user,token):
                raise serializers.ValidationError('Token is not valid or Expired')
            
            user.set_password(password)
            user.save()
            return attrs
        except DjangoUnicodeDecodeError as identifier:
            PasswordResetTokenGenerator().check_token(user,token)
            raise serializers.ValidationError('Token is not valid or Expired') 

