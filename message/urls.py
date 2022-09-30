from django.urls import path

from . import views

urlpatterns = [
    
    path('welcome/', views.welcome, name="Welcome"),
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]

