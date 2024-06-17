from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomerViewSet, OrderViewSet, oidc_authenticate, oidc_callback


router = DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', oidc_authenticate, name="oidc_authenticate"),
    path('auth0/callback/', oidc_callback)
]

