from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from products.models import Product, Order


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    orders = serializers.StringRelatedField(
        many=True
    )
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'created_at', 'orders')
        validators = [
            UniqueTogetherValidator(
                queryset = Product.objects.all(),
                fields = ('name',),
                message = "The product name should be unique"
            )
        ]


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    product = serializers.PrimaryKeyRelatedField(source='product.name', read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'created_at', 'product')
