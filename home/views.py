from django.shortcuts import render 
from home.models import Contact 
from django.contrib import messages
from forest.models import Post
from django.contrib.postgres.search import SearchVector , SearchRank , SearchQuery

def home(request):
    return render(request , 'home/home.html')
def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        content = request.POST['content']
        # checking every details are fine
        if len(name) < 3:
            messages.error(request , "You'r name is incorrect")
        elif len(email) < 10:
            messages.error(request , "You'r email is wrong")
        elif len(content) < 1:
            messages.error(request , "You need to put at least one character on you'r descreption")
        else:
            contact = Contact(name = name , email = email , number = number , content = content)
            contact.save()
            messages.success(request , "You message has been send You will be replayed on you gmail")
    return render(request , 'home/contact.html')
def about(request):
    return render(request , 'home/about.html')
def login(request):
    return render(request , 'home/login.html')
def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
    
    return render(request , 'home/register.html')

def search(request):
    # checking if request is post and from our official site 
    
    # if request is from our site recheck request is from search button 
    # getting query 
    query = request.GET["search"]
    # check if query is longer than 70 worlds 
    if len(query)>70:
        search_related_posts = Post.objects.none()
    else:
        # fetching related posts form database with diffrent colomn's 
        # search_from_title = Post.objects.filter(title__icontains = query)
        # search_from_content = Post.objects.filter(content__icontains = query)
        # search_from_category = Post.objects.filter(category__icontains = query)
        # search_from_section = Post.objects.filter(section__icontains = query)
        # joining all search column's with each others 
        # search_related_posts = search_from_title.union(search_from_category , search_from_section ,search_from_content )
        vector = SearchVector("title" , weight = "A") + \
            SearchVector("content", weight = "B")
        q = SearchQuery(query)
        search_related_posts = Post.objects.annotate(rank=SearchRank(vector , q , cover_density = True)).order_by("-rank")
    # checking if search_related_posts are empty 
    if search_related_posts.count() == 0:
        messages.error(request , "No content found, Please recheck you query")
    # seding context 
    context = {"search_related_posts": search_related_posts , "query":query}
    # render search.html if request is post means request is from our site  
    return render(request , "home/search.html" , context)
    


