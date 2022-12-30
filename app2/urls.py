from django.urls import path
from app2.views import *
app_name='details'

urlpatterns=[
    path('details/',details,name='details'),
]