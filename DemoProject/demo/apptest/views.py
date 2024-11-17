from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
def index(request):
    return HttpResponse("Hello world. Siuuuuu.");

def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info
    
    response = HttpResponse()
    response.headers['Age'] = 20

    msg  = f"""<br>
        <br>Path: {path}
        <br>Address: {address}
        <br>Scheme: {scheme}
        <br>Method: {method}
        <br>User Agent: {user_agent}
        <br>Path Info: {path_info}
        <br>
        <br>Response header: {response.headers}

    """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')

def pathview(request, name, id):
    return HttpResponse("Name: {} User Id:{}".format(name, id))


def qryview(request):
    name = request.GET['name']
    id = request.GET['id']
    return HttpResponse("Name: {}, UserId: {}".format(name, id))


def showform(request):
    return render(request, "apptest/form.html")


def getform(request):
    if request.method == "POST":
        id=request.POST['id']
        name=request.POST['name']
    return HttpResponse("Name: {}, UserId:{}".format(name,id))

def menuitems(request,dish):
    items = {
        'pasta': 'Pasta is a type of noodle',
        'falafel': 'Falafel are a deep fried patties',
        'cheesecake': 'Cheese cake is a cake'
    }

    description = items[dish]

    return HttpResponse(f"<h2>{dish}</h2>" + description)