from rest_framework import serializers
from .models import NewContact,Product,Order,OrderUpdate


class ContactSerilizer(serializers.ModelSerializer):
    class Meta:
        model = NewContact
        fields = ['name','email','phone','desc']


class ProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id','product_name','category','price','image','desc','pub_data']

class SingleProductSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['product_id','product_name','category','price','image','desc','pub_data']

        
class CategoryWiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product    
        fields = ['product_id', 'product_name', 'category', 'price', 'image', 'desc', 'pub_data']


class OrderSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderUpdateSerilizer(serializers.ModelSerializer):
    class Meta:
        model = OrderUpdate
        fields = '__all__'

class OrderSerilizerTracker(serializers.ModelSerializer):
    class Meta:
        model= Order
        fileds = '__all__'

class OrderJsonSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['items_json']