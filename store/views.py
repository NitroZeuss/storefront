from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import Product, Customer, Collection, reviews
from .serializers import ProductSerializer, CustomerSerializer, CollectionSerializer, ReviewSerializer

# Product list View logic
class ProductViewSet(ModelViewSet):
    queryset =Product.objects.all()
    serializer_class =ProductSerializer

    def get_serializer_context(self):
         return {'request': self.request}

    def delete(self, request, pk):
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









