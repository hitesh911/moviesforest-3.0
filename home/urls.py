from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact , name='contact'),
    path('about', views.about , name='about'),
    path('disclaimer', views.disclaimer , name='disclaimer'),
    path('dmca', views.dmca , name='dmca'),
    path('search', views.search , name='search'),
    path('history', views.history , name='history'),
    path("ZeroTwo", views.ZeroTwo.as_view(), name="ZeroTwo"),
    
]
