from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter
from django.urls import path, include
from rest_framework_nested import routers
from . import views

router = SimpleRouter()
router.register('products', views.ProductViewSet, basename='products')
router.register('collections', views.CollectionViewSet)
router.register('cart', views.CartViewset, basename='cart')
router.urls

products_router = routers.NestedDefaultRouter(router, "products", lookup='products')
products_router.register('reviews', views.ReviewViewset, basename='product-reviews')

urlpatterns = router.urls + products_router.urls