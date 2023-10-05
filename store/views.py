from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer  # Correct the import if caused by a typo/spelling mistake
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])
def product_detail(request, id):
    if request.method == 'GET':
        product = Product.objects.get(pk=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    else:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data()
            return Response('Check. Clear to go')
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def product_list(request):
    queryset = Product.objects.select_related('collection').all()
    serializer = ProductSerializer(queryset, many=True)
    return Response(serializer.data)
