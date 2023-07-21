from django.urls import path
from app1.views import *

app_name='somthing'

urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]