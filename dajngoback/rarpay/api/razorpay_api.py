from rest_framework.views import APIView
from rest_framework import status
from .razorpay_serilizre import CreateOrderSerializer,TranctionSerilizer
from rest_framework.response import Response
from rarpay.api.rpay.main import RazorPayClient  # Corrected import path
from django.shortcuts import HttpResponse

rz_client = RazorPayClient()

class CreateOrderApiView(APIView):
    def post(self, request):
        print(request.data)

        create_order_serilizer = CreateOrderSerializer(data=request.data)
        if create_order_serilizer.is_valid():
            order_response = rz_client.create_order(  # Check the method name for creating an order
                amount=create_order_serilizer.validated_data.get("amount"),
                currency=create_order_serilizer.validated_data.get("currency")
            )
            
            response = {
                "status_code": status.HTTP_200_OK,
                "message": "order_created",
                "data": order_response
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            response = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                'message': 'bad request',
                'error': create_order_serilizer.errors
            }
        # return HttpResponse('ok')
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

class TranctionApiView(APIView):
    def post(self,request):
        tranction_serilizer = TranctionSerilizer(data=request.data)
        if tranction_serilizer.is_valid():
            rz_client.verify_payment(
                razorpay_order_id=tranction_serilizer.validated_data.get("order_id"),
                razorpay_payment_id=tranction_serilizer.validated_data.get("payment_id"),
                razorpay_signature=tranction_serilizer.validated_data.get("signature")

            )
            tranction_serilizer.save()
            response = {
                "status_code":status.HTTP_201_CREATED,
                "message":"tranction created",
            }
            return Response(response,status=status.HTTP_201_CREATED)
        else:
            response={
                "status":status.HTTP_201_CREATED,
                "message":"bad request",
                "error": tranction_serilizer.errors
            }
            return Response(response,status=status.HTTP_400_BAD_REQUEST)
        
    