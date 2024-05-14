# Create your views here.
# api/views.py

from rest_framework import viewsets
from .serializers import ProductSerializer, OrderSerializer, UserSerializer, PaymentSerializer
from products.models import Product
from orders.models import Order
from users.models import User
from payments.models import Payment

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
