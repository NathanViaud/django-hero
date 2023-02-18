from django.shortcuts import redirect
from django.urls import path
from django.views.generic import RedirectView
from . import views


app_name = 'book'

urlpatterns = [
    path('', views.index, name='index'),
    path('page/0', RedirectView.as_view(url='charactercreation')),
    path('page/<int:pk>', views.PageView.as_view(), name='page'),
    path('page/charactercreation', views.characterCreation, name='charactercreation'),
]