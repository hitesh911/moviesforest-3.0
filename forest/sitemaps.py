from django.contrib.sitemaps import Sitemap
from forest.models import Post
# this is a class which inharrit the django contrib sitemap class for all dinamic urls 
class PostSitemap(Sitemap):
    protocol = "https"
    def items(self):
        return Post.objects.all()
    def location(self , obj):
        return f"/forest/download?post_id={obj.sno}"