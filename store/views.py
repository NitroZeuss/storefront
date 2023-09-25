from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializers
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST'])
def product_list(request):
    product = Product.objects.get(pk=id)
    serializer = ProductSerializers(product)
    return Response(serializer.data)
