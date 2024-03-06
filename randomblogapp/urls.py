

from django.contrib import admin
from django.urls import path
from .views import randombtnfunc

urlpatterns = [
    path("randombtn/", randombtnfunc, name='randombtn'),
]
