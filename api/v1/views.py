from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import generics
from products.models import Product, Order
from .serializer import ProductSerializer, OrderSerializer
 
    
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        DjangoFilterBackend,  
        filters.OrderingFilter,
        filters.SearchFilter
    ]


class ProductObject(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductObjectDelete(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductObjectChange(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all().select_related('product')
    serializer_class = OrderSerializer
    lookup_field = 'product__name'

