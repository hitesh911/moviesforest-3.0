from django.contrib import admin
from django.urls import path 
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('contact', views.contact , name='contact'),
    path('about', views.about , name='about'),
    path('disclaimer', views.disclaimer , name='disclaimer'),
    path('dmca', views.dmca , name='dmca'),
    path('search', views.search , name='search'),
    path('history', views.history , name='history'),
    path("jquery_search", views.jquery_search, name="jquery_search"),
    path("ZeroTwo", views.ZeroTwo.as_view(), name="ZeroTwo"),
    # this is a path to send notification 
    path("send_notification", views.send_notification, name="send_notification")
    
]
