from rest_framework import serializers
from .models import KartComment


class BlogCommentSerlilizer(serializers.ModelSerializer):
    class Meta:
        model = KartComment
        fields = ['sno','comment','user','product','time']

    
 
class BlogReplySerilizer(serializers.ModelSerializer):
    class Meta:
        model = KartComment
        fields = '__all__'

