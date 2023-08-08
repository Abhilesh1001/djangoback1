from rest_framework import serializers
from customauth.models import User

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


