from rest_framework import serializers
from .models import Product
from decimal import Decimal
from .models import Collection


class ProductSerializer(serializers.ModelSerializer):
    price_with_tax = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price', 'price_with_tax', 'collection']

    @staticmethod
    def get_price_with_tax(product):
        return product.unit_price * Decimal(1.1)


class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title']
