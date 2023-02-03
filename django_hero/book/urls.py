from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('page/<int:pk>', views.PageView.as_view(), name='page'),
    path('characterform', views.characterForm, name='characterform'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register')
]