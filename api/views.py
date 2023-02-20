from rest_framework import views, status
from rest_framework.response import Response
from .models import Account, Store, Products, Categories, Customers, Orders
from .serializers import AccountSerializer, StoreSerializer, ProductSerializer, OrderSerializer
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
import uuid
from django.utils.text import slugify

class SignupAPI(views.APIView):
    authentication_classes = []
    permission_classes = []

    def post(self, request):
        # create account
        serializer = AccountSerializer(data=request.data)
        # issue token
        if serializer.is_valid():
            seller=serializer.save()
            # Generate token
            token, created = Token.objects.get_or_create(user=seller)
            return Response({"token": token.key}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)


class StoreCreationAPI(views.APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        # create store
        serializer = StoreSerializer(data=request.data)
        # issue token
        if serializer.is_valid():
            store=serializer.save(owner=request.user,link=slugify(serializer.validated_data['name'])+'/'+str(uuid.uuid1()))
            return Response({'store_id': store.id, 'store_link': store.link}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=400)


class InventoryUploadAPI(views.APIView):
    def post(self, request):
        category_name = request.data.get('category')
        # create category if it doesn't exist
        category, created = Categories.objects.get_or_create(
            name=category_name
        )
        request_data = request.data
        request_data['category'] = category.id
        serializer = ProductSerializer(data=request_data)
        # issue token
        if serializer.is_valid():
            product=serializer.save()
            return Response({'id': product.id, 'name': product.name, 'image': product.image}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=400)


class OrderAcceptView(views.APIView):
    def post(self, request):
        order_id = request.data.get('id')
        try:
            order = Orders.objects.get(id=order_id)
        except Orders.DoesNotExist:
            return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)

        order.status = 1
        order.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data, status=status.HTTP_200_OK)

