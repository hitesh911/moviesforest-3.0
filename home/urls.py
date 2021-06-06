from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact , name='contact'),
    path('about/', views.about , name='about'),
    path('login/', views.login , name='login'),
    path('register/', views.register , name='register'),
    path('search/', views.search , name='search'),
    path('history/', views.history , name='history'),
    path("ZeroTwo/", view.ZeroTwo.as_view(), name="ZeroTwo")
    
]
