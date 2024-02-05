from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter
from django.urls import path, include
from . import views

router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
router.urls

urlpatterns = router.urls