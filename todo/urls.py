from django.contrib import admin
from django.urls import path
from . import views

app_name = 'todo'

urlpatterns = [
    path('', views.home),
    path('weather', views.weather),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('login_page', views.login_page),
    path('signup_page', views.signup_page),
    path('edit/logout', views.logout),
    path('edit/<str:pk>', views.edit),
    path('delete/<str:pk>', views.delete),
    path('edit/update_task/<str:pk>', views.update_task),
    path('add_item/<str:pk>', views.add_item),
    path('edit/add_item/<str:pk>', views.add_item),
]
