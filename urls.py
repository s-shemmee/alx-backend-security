from django.contrib import admin
from django.urls import path
from ip_tracking.views import home_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="IP Tracking API",
        default_version='v1',
        description="API documentation for IP Tracking",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', __import__('ip_tracking.views').views.login_view),
    path('', home_view, name='home'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
