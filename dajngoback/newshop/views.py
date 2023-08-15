from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from customauth.renderers import UserRenderer
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serilizer import ContactSerilizer,ProductSerilizer,SingleProductSerilizer,CategoryWiseSerializer,OrderSerilizer,OrderUpdateSerilizer,OrderJsonSerilizer,CartDataSerilizer,CartCreateSerilizer
from .models import NewContact,Product,OrderUpdate,Order,CartUserData,ExcelFile
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
import pandas as pd
from django.http import JsonResponse
from django.conf import settings
from rest_framework.views import APIView
from .helpers import save_pdf
from django.http import FileResponse
from io import BytesIO
import openpyxl
# Create your views here.

class NewContactView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serilizer = ContactSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'Contact Saved SucessFully'},status=status.HTTP_200_OK)
        
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductView(APIView):
    renderer_classes=[UserRenderer]
    # permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        pro = Product.objects.all() 
        serilizer = ProductSerilizer(pro,many=True)
        return Response(serilizer.data)
            

class SingleProductView(APIView):
    renderer_classes=[UserRenderer]
    # permission_classes=[IsAuthenticated]
    def get(self,request,pk=None,format=None):
        pro = Product.objects.get(product_id=pk) 
        serilizer = SingleProductSerilizer(pro)
        return Response(serilizer.data)
    

class CategoryWiseView(APIView):
    renderer_classes = [UserRenderer]

    def get(self, request, format=None):
        categories = Product.objects.values_list('category', flat=True).distinct()
        # print(categories)

        # Query the products for each category and serialize the data
        category_wise_data = {}
        for category in categories:
            products = Product.objects.filter(category=category)
            # print(products)
            serializer = CategoryWiseSerializer(products, many=True)
            category_wise_data[category] = serializer.data
        
        # print(category_wise_data)

        return Response(category_wise_data)


class NewOrder(APIView):
    renderer_classes = [UserRenderer]
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        serilizer = OrderSerilizer(data=request.data)
        if serilizer.is_valid():
            order = serilizer.save()
            order_id = order.order_id
            orderupdate = OrderUpdate(order_id=order_id,update_desc='Your order has been placed')
            orderupdate.save()
            return Response({'order_id':order_id,'msg':'Order Saved SucessFully'},status=status.HTTP_200_OK)
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class OrderUpdateView(APIView):
    renderer_classes=[UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        order_id = request.data.get('order_id')
        email = request.data.get('email')
        # print(order_id,email)
        try:
            order = Order.objects.filter(order_id=order_id,email=email)
            dataSerilize = []
            if len(order) > 0:
                update = OrderUpdate.objects.filter(order_id=order_id)
                print(order)    
                serilizerData = OrderJsonSerilizer(order,many=True)
                serilizer = OrderUpdateSerilizer(update,many=True)
                data_serialize = {
                'order_updates': serilizer.data,
                'order': serilizerData.data
              }
                return Response(data_serialize)
        except Exception as e:
            return Response({'error':"Order not found"})
        return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)
    


class CartUpdateView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def put(self,request,email):
        try:
            instance = CartUserData.objects.get(user__email=email)
            serilizer = CartDataSerilizer(instance,data=request.data)
        except CartUserData.DoesNotExist:
            serilizer = CartDataSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data Updated Successfully'})
        
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)


class CartCreateView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        serilizer = CartCreateSerilizer(data=request.data)
        if serilizer.is_valid():
            serilizer.save()
            return Response({'msg':'data Created Successfully'})
        
        return Response(serilizer.errors,status=status.HTTP_400_BAD_REQUEST)



class GetCartView(APIView):
    renderer_classes =[UserRenderer]    
    # permission_classes = [IsAuthenticated]
    def get(self,request,email,format=None):
        try:
            pro = CartUserData.objects.get(user__email=email)
            serilizer = CartCreateSerilizer(pro)  
            return Response(serilizer.data)
        except Exception as e:
            return Response({'error':'error'})
        


def export_data_to_excel(request):
    objs = NewContact.objects.all()
    data = []
    for obj in objs:
        data.append({
            "name": obj.name,
            "email":obj.email,
            "phone" : obj.phone,
            "desc" : obj.desc
        })
    pd.DataFrame(data).to_excel('output.xlsx')
    return JsonResponse({
        'status': 200
    })


def export_to_excel_on_download(request):
    objs = NewContact.objects.all()
    data = []
    for obj in objs:
        data.append({
            'name':obj.name,
            'email': obj.email,
            'phone':obj.phone,
            'desc': obj.desc
        })
    
    # create a new Excel worbook and worksheet 
    workbook = openpyxl.Workbook()
    worksheet = workbook.active

    # write data to worksheet 
    for row_data in data:
        worksheet.append([row_data["name"], row_data["email"], row_data["phone"], row_data["desc"]])

    # create a Bytes data IO to hold the excel file content 
    buffer = BytesIO()

    # save the IO to the buffer 
    workbook.save(buffer)
    buffer.seek(0)
    response = FileResponse(buffer, as_attachment=True, filename='output.xlsx')

    return response 


def import_exce_in_folder(request):
    objs =NewContact.objects.all()
    data = []
    for obj in objs:
        data.append({
            'name':obj.name,
            'email': obj.email,
            'phone':obj.phone,
            'desc': obj.desc
        })

    if request.method == 'POST':
        # Get the user-specified filename from the POST data
        filename = request.POST.get('filename', 'output.xlsx')

        # Create a new Excel workbook and worksheet
        workbook = openpyxl.Workbook()
        worksheet = workbook.active

        # Write data to the worksheet
        for row_data in data:
            worksheet.append([row_data["name"], row_data["email"], row_data["phone"], row_data["desc"]])

        # Create a BytesIO buffer to hold the Excel file content
        buffer = BytesIO()

        # Save the workbook to the buffer
        workbook.save(buffer)
        buffer.seek(0)
        response = HttpResponse(buffer.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{filename}"'

        return response
    return render(request, 'your_template.html')


        
def import_data_to_db(request):
    if request.method == 'POST':
        file = request.FILES['files']
        obj = ExcelFile.objects.create(
            file =file
        )
        path = file.file 
        print(f'{settings.BASE_DIR}/{path}')
        df = pd.read_excel(path)
        print(df)
        for d in df.values:
            print(d)

    
    return render(request,'home.html')



class contact_pdf(APIView):
    def get(self,request):

        contacts = NewContact.objects.all()
        params = {
            'contacts': contacts
        }
        filename,status = save_pdf(params)

        if not status:
            return Response({'status':400})
        
        return Response({'status':200,'path':f'/media/{filename}.pdf'})





        