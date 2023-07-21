from django.urls import path
from app2.views import *
app2_name='nothing'


urlpatterns=[
    path('first/',first,name='first'),
    path('second/',second,name='second'),
]