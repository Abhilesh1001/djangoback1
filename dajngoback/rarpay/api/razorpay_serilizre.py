from rest_framework import serializers
from ..models import Tanctiction

class CreateOrderSerializer(serializers.Serializer):
    amount = serializers.IntegerField()
    currency = serializers.CharField()  # Assuming currency is a string, use CharField


class TranctionSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Tanctiction
        fields = "__all__"
