from django.urls import path
from . import views


app_name = 'book'

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<int:pk>', views.PageView.as_view(), name='page'),
    path('characterform', views.characterForm, name='characterform'),
]