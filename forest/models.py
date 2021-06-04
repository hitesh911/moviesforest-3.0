from django.db import models

# model to storeing the posts 
class Post(models.Model):
    # for serial number.
    sno = models.AutoField(primary_key= True)
    # this is for movie section 
    section = models.TextField(default= "hollywood" )
    # for categories
    category = models.TextField(default = "adventure") 
    # this is for logo 
    logo_link = models.TextField(default="https://parrotsec.org/images/about/notebook.png") 
    # field for screenshots links
    screen_shots = models.TextField(default = "https://parrotsec.org/images/about/notebook.png https://parrotsec.org/images/about/notebook.png https://parrotsec.org/images/about/notebook.png https://parrotsec.org/images/about/notebook.png ") 
    # this is for title 
    title = models.TextField(default= "temp")
    # this is for title caption 
    title_caption = models.TextField(default= "this is the caption for title")
    # this is for description 
    content = models.TextField(default="this i isis fd jfl jfjsal dsj oif ds fdjfk dlkjdsfk dsjfkl dsdflk dslkdsjflk dlkjflkds flk jdsflkdsjflkjfoier jfd.,j fl dsjflkjsod")
    # field for download links 
    download_links = models.TextField(default= ' {"480":"https://480", "720":"https://720","1080":"https://1080"}')
    # this is for trailers 
    trailer_link = models.TextField(default="https://tralerss")
    # this is for views 
    views_count = models.IntegerField(default=0)
    
    # this is for timestamp 
    timestamp = models.DateTimeField( blank = True, auto_now_add=True)




    def __str__(self):
        return " " + self.title

# model to storing the labels 
class Label(models.Model):
    # creating a CharField for saving all labels 
    categories = models.CharField(max_length=1000)

    def __str__(self):
        return " " + self.categories


    