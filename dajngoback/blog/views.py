from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from customauth.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from .serilizer import BlogCommentSerlilizer,BlogReplySerilizer
from .models import KartComment
from customauth.models import User
from newshop.models import Product

# Create your views here.
def index(request):
    return HttpResponse('Views Page')
    

class BlogComment(APIView):
    renderer_classes=[UserRenderer]
    # permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serilizer = BlogCommentSerlilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Blog comment save Successfully'},status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        

class BlogReply(APIView):
    renderer_classes=[UserRenderer]
    def post(self,request,format=None):
        serlilizer = BlogReplySerilizer(data=request.data)
        if serlilizer.is_valid():
            serlilizer.save()
            return Response({'msg':'Blog reply save Successfully'},status=status.HTTP_200_OK)
        return Response(serlilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class BlogCommentView(APIView):
    renderer_classes = [UserRenderer]   
    def get(self,request,pk=None,format=None):
        obj=KartComment.objects.filter(product__product_id=pk,parent__isnull=True)
        replies=KartComment.objects.filter(product__product_id=pk).exclude(parent=None)

        
        repDict ={}
        for reply in replies:
            if reply.parent.sno not in repDict.keys():
                formatted_time = reply.time.strftime('%d %m %Y %H:%M')
                print(reply.sno)
                comment_dict = {
                'sno': reply.sno,
                'comment': reply.comment,
                'user': reply.user.name,  # Fetch the user's name
                'time':formatted_time,
                }
                repDict[reply.parent.sno]=[comment_dict]
            else:
                formatted_time = reply.time.strftime('%d %m %Y %H:%M')  # Move this line here
                comment_dict = {
                'sno': reply.sno,
                'comment': reply.comment,
                'user': reply.user.name,  # Fetch the user's name
                'time':formatted_time,
                }
                repDict[reply.parent.sno].append(comment_dict) 
        
        # print('rep',repDict)
        cart_comment = []
        for comment_info in obj:
            formatted_time = comment_info.time.strftime('%d %m %Y %H:%M')

            comment_dict = {
                'sno': comment_info.sno,
                'comment': comment_info.comment,
                'user': comment_info.user.name,  # Fetch the user's name
                'time':formatted_time,
            }
            cart_comment.append(comment_dict)
        cart=   {
            "cart_comment" :cart_comment,
            "reply_comment" : [repDict]
        }
        # print('cart',cart)

        return Response(cart)

