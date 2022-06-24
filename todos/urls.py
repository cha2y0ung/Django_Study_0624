from django.urls import path
from .views import *

urlpatterns = [
    path('',todolist, name='list'),
    path('create/', todocreate, name='create'),
]
