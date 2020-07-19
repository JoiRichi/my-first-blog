from django.urls import path

from . import views

urlpatterns = [
    path('', views.another, name='nextpage'),
]