from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('blog/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('blog/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

