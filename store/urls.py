
from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('products/<int:id>/', views.product_detail),
    path('products/', views.product_list)
    # Other URL patterns...
]

