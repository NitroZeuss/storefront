from decimal import Decimal
from operator import itemgetter
from store.models import Product, Collection, Customer, reviews, CartItem
from .import models
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

    price_with_tax = serializers.SerializerMethodField(method_name='calculate_tax')

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


class SimpleProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'unit_price']



class CartItemSerializer(serializers.ModelSerializer):
    product = SimpleProductSerializer()
    total_price = serializers.SerializerMethodField(method_name='calculate_total_price')

    class Meta: 
        model = CartItem
        fields = ['cart', 'product', 'quantity', 'total_price']

    def calculate_total_price(self, cart_item: CartItem):
        return cart_item.product.unit_price * cart_item.quantity

    


class CartSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    item = CartItemSerializer(many=True)
    total_price = serializers.SerializerMethodField(method_name="get_total_price")

    def get_total_price(self, cart):
        return cart.total_price  # Assuming total_price is a field in the Cart model

    class Meta:
        model = models.Cart
        fields = ['id', 'item', 'total_price']
