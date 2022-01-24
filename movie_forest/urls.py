"""movie_forest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include 
from django.contrib.sitemaps.views import sitemap
from movie_forest.sitemaps import PostSitemap
# importing template view for robots.txt 
from django.views.generic.base import TemplateView

sitemaps = {
    "link":PostSitemap
}
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('forest/', include('forest.urls')),
    # making a sitemap.xml url 
    path('sitemap.xml',sitemap,{"sitemaps":sitemaps}, name = 'django.contrib.sitemaps.views.sitemap'),
    # making robots.txt url 
    path("robots.txt", TemplateView.as_view(template_name = "robots.txt",content_type = "text/plain"), name="robots.txt"),
    # this is for weppush application 
    path("webpush", include("webpush.urls")),
]

handler404 = "home.views.error_404"
handler500 = "home.views.error_500"
handler403 = "home.views.error_403"
handler400 = "home.views.error_400"