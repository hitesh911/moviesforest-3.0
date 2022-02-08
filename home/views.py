from django.shortcuts import render  , HttpResponse
from django.http import JsonResponse
from django.views import View
from home.models import Contact 
from django.contrib import messages
from forest.models import Post
from django.contrib.postgres.search import SearchVector , SearchRank , SearchQuery
from forest.views import get_labels , color_list
# importing get clint ip function for history function
from forest.views import get_client_ip
import requests , time
# this is a function from webpush applocation 
from webpush import send_group_notification

# this is the function for sending notifications to subscribers 
def send_notification(request):
    # inisilizing status 
    notification_send = True
    problem = None
    # getting data from request 
    try:
        heading = request.GET["heading"]
        body = request.GET["body"]
        icon_url = request.GET["icon_url"]
        url =request.GET["url"]
    except Exception as e:
        problem = str(e)
    if problem == None:
        # deciding for which group i want to send the notification 
        group_name = "my_subscriber"
        # making a data payload to send content in notification 
        payload = {"head": heading, "body": body, 
            "icon": icon_url, "url": url}
        try:
            send_group_notification(group_name=group_name, payload=payload, ttl=10000)
        except:
            notification_send = False
    else:
        notification_send = False
    
    # making a context 
    context = {"Notification_send": notification_send,
                "problem" : problem
    
    }
    return JsonResponse(context)

# funcitons to handel kinds of erros 
def error_500(request):
    label_object = get_labels()
    context = {"year": label_object["year"] ,"main":label_object["main"] ,  "other":label_object["other"] ,}
    return render(request, "errors/error_500.html" , context)
def error_404(request , exception):
    label_object = get_labels()
    context = {"year": label_object["year"] ,"main":label_object["main"] ,  "other":label_object["other"] ,}
    return render(request, "errors/error_404.html" , context)
def error_403(request , exception):
    label_object = get_labels()
    context = {"year": label_object["year"] ,"main":label_object["main"] ,  "other":label_object["other"] ,}
    return render(request, "errors/error_403.html" , context)
def error_400(request , exception):
    label_object = get_labels()
    context = {"year": label_object["year"] ,"main":label_object["main"] ,  "other":label_object["other"] ,}
    return render(request, "errors/error_400.html" , context)


def home(request):
    # logic for show trending movies 
    trending_movies = Post.objects.all().order_by("views_count").reverse()[:4]
    # getting the list of indexes 
    all_movies =  Post.objects.all().order_by("sno").reverse()
    # messages.success(request , "<a class = 'text-deco`ration-none' href = 'http://moviesforest.herokuapp.com'>Click here <a/>for better experince")
    # ---------------------this is the content related to the wepush notifications -----------------
    # deciding a goup name for my subscribers 
    group_name = "my_subscriber"
    # making a dict of group to send it to context 
    webpush = {"group": group_name}
    # getting labels 
    label_object = get_labels()
    # getting labels content 
    # initilizing default categories_data dict
    categories_data = {}
    # getting list of other labels containing names
    other = label_object["main"]
    # making a categories_data object of name of label and its posts querset 
    for cats in other:
        cats_post = Post.objects.filter(category__icontains=cats).order_by("sno").reverse()
        if len(cats_post) != 0:
            categories_data[cats] = cats_post
    # making a context 
    context = {"categories_data":categories_data, "color_list": color_list,"trending_movies":trending_movies,"all_movies":all_movies,"webpush":webpush,  "year": label_object["year"] ,"main":label_object["main"] ,  "other":label_object["other"] ,}
    #-------------------------- returning the context with goup name for webpush --------------------------------
    return render(request , 'home/home.html', context)
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
    label_object = get_labels()
    context = { "year": label_object["year"] ,"main":label_object["main"] ,  "other":label_object["other"] ,}
    return render(request , 'home/contact.html'  , context)
def about(request):
    label_object = get_labels()
    context = { "year": label_object["year"] ,"main":label_object["main"] ,  "other":label_object["other"] ,}
    return render(request , 'home/about.html' , context)
def dmca(request):
    label_object = get_labels()
    context = { "year": label_object["year"] ,"main":label_object["main"] ,  "other":label_object["other"] ,}
    return render(request , 'home/dmca.html' , context)
def disclaimer(request):
    label_object = get_labels()
    context = { "year": label_object["year"] ,"main":label_object["main"] ,  "other":label_object["other"] ,}
    return render(request , 'home/disclaimer.html' , context)


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
    # getting label 
    label_object = get_labels()
    # seding context 
    context = {"color_list": color_list,"search_related_posts": search_related_posts , "query":query, "year": label_object["year"] ,"main":label_object["main"] ,  "other":label_object["other"] ,}
    # render search.html if request is post means request is from our site  
    return render(request , "home/search.html" , context)
# this is for search suggestions 
def jquery_search(request):
    query = request.GET.get("term")
    # normal title search from database for suggestions:
    search_related_posts = Post.objects.filter(title__icontains = query)
    title_list = []
    title_list += [x.title for x in search_related_posts]
    return JsonResponse(title_list , safe=False)
# this is for history save 
def history(request):
    messages.warning(request , "You'r history will deleted with ip change")
    current_user_ip = str(get_client_ip(request = request))
    history_related_posts = Post.objects.filter(ips__icontains = current_user_ip)
    # getting labels 
    label_object = get_labels()
    context = {"color_list": color_list, "history_related_posts":history_related_posts, "year": label_object["year"] ,"main":label_object["main"] ,  "other":label_object["other"] ,}
    return render(request , "home/history.html" , context)



# making a class for zeroTwo 
class ZeroTwo(View):
    def get(self , request):
        response = "You can't access ZeroTwo like this motherfucker!"
        # getting labels 
        label_object = get_labels()
        context = {"getresponce":response,  "year": label_object["year"] ,"main":label_object["main"] ,  "other":label_object["other"] ,}
        return render(request , "home/zero_two.html" , context)
    def post(self , request):
        messages.warning(request , "Zero_Two's content is not verifyed. It could be wrong")
        # making default context verables 
        name = None
        size = None
        link = None
        status = False
        request_success = True
        movies_array = []
        # getting user define movie name 
        movie_name = str(request.POST["movie"]).replace(" ", "+")
        # getting year 
        year = str(request.POST["year"]).replace(" ", "+")
        # base url to request to zero_two 
        base_url = 'http://zerotwo.gq'
        # search path 
        base_path = "/search/movie"
        # api is to acess the zerotwo
        api_id = "1068352349"
        # api key to excess the zero_two api 
        api_key = 'DYw7jYeBB08nzz4rr7gUDpNoIuczSFzAr2ri0eVwRLY='
        # making a query to search in zero_two 
        query = f"{movie_name}+{year}"
        # making a perfect url to make first request 
        url1 = f'{base_url}{base_path}'
        # headers for request
        head = {
            'id' : api_id,
            'key' : api_key,
            'movie_name' : query
        }
        # making a request to zero_two api 
        try:
            data1 = requests.get(url1,headers=head).json()
        except:
            request_success = False
            
        # sleeping for 5 second for second request 
        time.sleep(5)
        
        # if first request status is True so ony then make second request 
        if request_success:
            status = data1["status"]
            if status:
                movies_array = data1["links"]
            else:
                pass
        else:
            pass
        # getting labels 
        label_object = get_labels()
        context = {"movies_array":movies_array,"request_success":request_success, "status":status, "query":query, "year": label_object["year"] ,"main":label_object["main"] ,  "other":label_object["other"] ,}
        return render(request , "home/zero_two.html" , context)


