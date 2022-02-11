from sys import path_hooks
from xml.etree.ElementInclude import include
from django.urls import path

from . import views

app_name='ledger'
urlpatterns = [
    path('', views.index, name='index'),
    path('page1/', views.page1, name='page1'),
    path('page2/', views.page2, name='page2'),
]
