from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework import filters, generics
from rest_framework.decorators import permission_classes
from products.models import Product, Order
from .serializer import ProductSerializer, OrderSerializer
 
@permission_classes([AllowAny])    
class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [
        DjangoFilterBackend,  
        filters.OrderingFilter,
        filters.SearchFilter
    ]

@permission_classes([AllowAny]) 
class ProductObject(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@permission_classes([IsAdminUser]) 
class ProductObjectDelete(generics.RetrieveDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@permission_classes([IsAdminUser]) 
class ProductObjectChange(generics.RetrieveUpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@permission_classes([IsAdminUser])
class ProductCreate(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

@permission_classes([IsAuthenticatedOrReadOnly])
class OrderView(generics.ListCreateAPIView):
    queryset = Order.objects.all().select_related('product')
    serializer_class = OrderSerializer
    lookup_field = 'product__name'

