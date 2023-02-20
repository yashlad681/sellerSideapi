from rest_framework import serializers
from .models import Account,Store,Products,Orders,OrderItems

# Account Serializer for mobile number and OTP
class AccountSerializer(serializers.ModelSerializer):
    def validate(self, data):       
        if Account.objects.filter(mobile_number=data['mobile_number']).exists():
            raise serializers.ValidationError("User with same mobile number already exists.")
        return data


    class Meta:
        model = Account
        fields = ['mobile_number']


# Store Serializer for store name and address
class StoreSerializer(serializers.ModelSerializer):
    def validate(self, data):       
        if Store.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError("Store with same name already exists.")
        return data

    class Meta:
        model = Store
        fields = ['name', 'address']

class ProductSerializer(serializers.ModelSerializer):
    def validate(self, data):       
        if Products.objects.filter(name=data['name']).exists():
            raise serializers.ValidationError("Product with same name already exists.")
        return data

    class Meta:
        model = Products
        fields = ['name', 'description', 'mrp', 'sale_price', 'image','category','store' ]


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Orders
        fields = '__all__'