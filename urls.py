from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', __import__('ip_tracking.views').views.login_view),
]
