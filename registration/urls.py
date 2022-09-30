from django.urls import path

from . import views

urlpatterns = [
    path('', views.registration, name='Registration'),
    path('login/', views.loginpage, name='Login'),
    path('logout/', views.logOutUser, name="Logout"),
  
]

