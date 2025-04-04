from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    path('wheather', views.wheather),
    path('index2', views.page_itwo),
    path('about2', views.page_atwo),
    path('wheather2', views.page_wtwo)
]
    