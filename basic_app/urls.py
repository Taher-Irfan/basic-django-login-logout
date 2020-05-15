from django.contrib import admin
from django.urls import path, include
from .import views


app_name = 'basic_app'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('', views.index, name='index'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='logout'),
]
