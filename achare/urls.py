from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import permissions

from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework_simplejwt import views as jwt_views

from django.contrib import admin
from django.urls import path, include

schema_view = get_schema_view(
    openapi.Info(
        title='Achare Server API',
        default_version='v1',
        description='API For The Project',
        contact=openapi.Contact(email='sajad.tohidi76@gmail.com'),
        license=openapi.License('MIT License')
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0)),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


admin.site.site_header = 'Achare Server API Admin'
admin.site.site_title = 'Achare ServerAPI Admin Portal'
admin.site.index_title = 'Welcome to Achare'
