from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', include('event.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  
    path('', include('event.urls')),
]
