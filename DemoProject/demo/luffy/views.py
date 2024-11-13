from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def luffy(request):
    return HttpResponse("Monkey D. Luffy")

# def menu_by_id(request, id):
#     menu = Menu.objects.get(pk=id)
#     return HttpResponse(f"{menu.menu_item}: Type of {menu.cuisine} cuisine")