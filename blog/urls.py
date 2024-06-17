from django.urls import path
from .views import oidc_authenticate, oidc_callback


urlpatterns = [
  path('auth/', oidc_authenticate, name="oidc_authenticate"),
  path('auth0/callback/', oidc_callback)
]