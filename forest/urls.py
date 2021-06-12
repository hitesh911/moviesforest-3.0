from django.contrib import admin
from django.urls import path 
from forest import views

urlpatterns = [
    path('', views.forest_movies , name='movies'),
    path('movies', views.forest_movies , name='movies'),
    path('make_post', views.make_post , name='make_post'),
    path('download', views.download , name='download'),
    path('stream', views.stream , name='stream'),
    path('delete_post', views.delete_post , name='delete_post'),
    path('update_post', views.update_posts , name='update_post'),
    
]
