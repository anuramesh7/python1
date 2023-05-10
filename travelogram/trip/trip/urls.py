from django.conf import settings
from django.conf.urls.static import static

from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
    #path('add/',views.operations,name='operations'),
    #path('add/',views.sub,name='sub')

]
