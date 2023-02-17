from django.urls import path
from . import views


app_name = 'book'

urlpatterns = [
    path('', views.index, name='index'),
    path('page/', views.page, name='page'),
    path('characterform', views.characterForm, name='characterform'),
]