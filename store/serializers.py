from decimal import Decimal
from store.models import Product, Collection, Customer, reviews
from rest_framework import serializers


class CollectionSerializer(serializers.ModelSerializer):
    products_count = serializers.SerializerMethodField()

    class Meta:
        model = Collection
        fields = ['id', 'title', 'products_count']

    def get_products_count(self, obj):
        # Assuming you have a related name 'products' on your Collection model
        return obj.products.count()



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'slug', 'inventory', 'unit_price', 'price_with_tax', 'collection']

    price_with_tax = serializers.SerializerMethodField(
        method_name='calculate_tax')

    def calculate_tax(self, product: Product):
        return product.unit_price * Decimal(1.1)
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'first_name', 'last_name', 'email','phone', 'birth_date', 'membership']

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = reviews
        fields = '__all__'
   