from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ModelViewSet
from .models import Product, Customer, Collection, reviews
from .serializers import ProductSerializer, CustomerSerializer, CollectionSerializer, ReviewSerializer
from django_filters.rest_framework import DjangoFilterBackend


# Product View logic
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()  # Corrected queryset
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['collection_id']
    
    def get_serializer_context(self):
        return {'request': self.request} 

    def destroy(self, request, pk):  # Corrected to use destroy method
        product = get_object_or_404(Product, pk=pk)
        product.delete()
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











