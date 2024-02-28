from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Product, Customer, Collection, reviews, Cart
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from .serializers import ProductSerializer, CustomerSerializer, CollectionSerializer, ReviewSerializer, CartSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter  # Make sure this import is before ProductViewSet
from rest_framework.pagination import PageNumberPagination

from django_filters.rest_framework import FilterSet  # Import FilterSet separately if not already imported

# Product View logic
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()  # Corrected queryset
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    pagination_class = PageNumberPagination
    search_fields = ['title']
    ordering_fields = ['unit_price']
    
    def get_serializer_context(self):
        return {'request': self.request} 

    def destroy(self, request, pk):  # Corrected to use destroy method
        product = get_object_or_404(Product, pk=pk)
        product.delete()  # Corrected method call
        return Response(status=status.HTTP_204_NO_CONTENT)




# Collection list View logic
class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class =CollectionSerializer

    def delete(self, request, pk):
        collection_instance = self.get_object()  # Get the specific instance
        collection_instance.delete()
        return Response('Deleted!')

class ReviewViewset(ModelViewSet):
    queryset = reviews.objects.all()
    serializer_class = ReviewSerializer

# Cart View logic
    
class CartViewset(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def delete(self, request, pk):
        cart_instance = self.get_object()  # Get the specific instance
        cart_instance.delete()
        return Response('Deleted!')
        











