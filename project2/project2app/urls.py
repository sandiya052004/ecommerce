from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='IN1'),
    path('index1/',index11,name='index')
    
]
