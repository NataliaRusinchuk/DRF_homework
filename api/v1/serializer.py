from rest_framework import serializers
from products.models import Product, Order


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    orders = serializers.StringRelatedField(
        many=True
    )
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'created_at', 'orders')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.PrimaryKeyRelatedField(source='product.name', read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'created_at', 'product')
