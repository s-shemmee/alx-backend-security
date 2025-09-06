from django.contrib import admin
from django.urls import path
from ip_tracking.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', __import__('ip_tracking.views').views.login_view),
    path('', home_view, name='home'),
]
