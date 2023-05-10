"""tripproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include

from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('trip.urls')),
    path('cred/',include('cred.urls')),

]
if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL,
                         document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)