from . import views
from django.urls import path, include

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('thanks/',views.thanks,name='thanks')
    ]