from django.urls import path, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.FlowerLanding,name='main'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)