from django.shortcuts import render  , HttpResponse
from django.views import View
from home.models import Contact 
from django.contrib import messages
from forest.models import Post
from django.contrib.postgres.search import SearchVector , SearchRank , SearchQuery
# importing get clint ip function for history function
from forest.views import get_client_ip
import requests , time

def home(request):
    # messages.success(request , "<a class = 'text-deco`ration-none' href = 'http://moviesforest.herokuapp.com'>Click here <a/>for better experince")
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
def dmca(request):
    return render(request , 'home/dmca.html')
def disclaimer(request):
    return render(request , 'home/disclaimer.html')

def search(request):
    # checking if request is post and from our official site 
    
    # if request is from our site recheck request is from search button 
    # getting query 
    query = request.GET["search"]
    # if query is only widespaces or empty so giving all content in reversed format to tsukasa
    if query.isspace() or query == "":
        search_related_posts = Post.objects.all().order_by("sno").reverse()
    else:
        # check if query is longer than 70 worlds 
        if len(query)>70:
            search_related_posts = Post.objects.none()
        else:
            # advance vector search from postgres database :
            # making a vector of column's 
            vector = SearchVector("title" , weight = "A") + \
                SearchVector("content", weight = "B") + \
                    SearchVector("section" , weight = "C") + \
                        SearchVector("category" , weight = "D")
            # passing our query into SeaschQuery postgress function 
            q = SearchQuery(query)
            # making a final search results 
            search_related_posts = Post.objects.annotate(rank=SearchRank(vector , q , cover_density = True)).filter(rank__gte=0.3).order_by("-rank")
        # checking if search_related_posts are empty after advcance search so search it normally
        if search_related_posts.count() == 0:
            # normal search from database :
            # fetching related posts form database with diffrent colomn's 
            search_from_title = Post.objects.filter(title__icontains = query)
            search_from_content = Post.objects.filter(content__icontains = query)
            search_from_category = Post.objects.filter(category__icontains = query)
            search_from_section = Post.objects.filter(section__icontains = query)
            # joining all search column's with each others using union function
            search_related_posts = search_from_title.union(search_from_category , search_from_section ,search_from_content )
            # if search_related_posts is still empty giving an alert 
            if search_related_posts.count()==0:
                messages.error(request , "No content found, Please recheck you query")
            else:
                pass
        else:
            pass
    # seding context 
    context = {"search_related_posts": search_related_posts , "query":query}
    # render search.html if request is post means request is from our site  
    return render(request , "home/search.html" , context)
    
# this is for history save 
def history(request):
    messages.warning(request , "You'r history will deleted with ip change")
    current_user_ip = str(get_client_ip(request = request))
    history_related_posts = Post.objects.filter(ips__icontains = current_user_ip)
    context = {"history_related_posts":history_related_posts}
    return render(request , "home/history.html" , context)



# making a class for zeroTwo 
class ZeroTwo(View):
    def get(self , request):
        response = "You can't access ZeroTwo like this motherfucker!"
        context = {"getresponce":response}
        return render(request , "home/zero_two.html" , context)
    def post(self , request):
        messages.warning(request , "Zero_Two's content is not verifyed. It could be wrong")
        # making default context verables 
        name = None
        size = None
        link = None
        status = True
        request_success = True
        # getting user define movie name 
        movie_name = str(request.POST["movie"]).replace(" ", "+")
        # getting year 
        year = str(request.POST["year"]).replace(" ", "+")
        # getting size 
        size = request.POST["size"]
        # base url to request to zero_two 
        base_url = 'http://maiis.pythonanywhere.com'
        # api key to excess the zero_two api 
        API_KEY = '898sdvi7rb3l34cv'
        # making a query to search in zero_two 
        query = f"{movie_name}+{year}"
        # making a perfect url to make first request 
        url1 = f'{base_url}/api/{API_KEY}/search_movie/{query}/size={size}'
        # making a request to zero_two api 
        data1 = requests.get(url1).json()
        # sleeping for 5 second for second request 
        time.sleep(5)
        # if first request status is True so ony then make second request 
        if data1["status"]:
            # making next url to request 
            url2 = f'{base_url}/api/{API_KEY}/get_movie/{data1["key"]}'
            # making next request 
            data2 = requests.get(url2).json()
             # checking if zero_two get the movie 
            if data2['status']:
                name = data2["name"]
                size = data2["size"]
                link = data2["link"]
                status = data2["status"]
            # if zero_two did't get the movie so making status false 
            else:
                status = False
        # if first request status is not true so making request status false 
        else:
            request_success = False
       
        context = {"request_success":request_success, "status":status,"name":name,
                    "size":size , "link":link , "query":query}
        return render(request , "home/zero_two.html" , context )
