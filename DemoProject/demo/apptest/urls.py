from django.urls import path, re_path
from . import views 

app_name='apptest'

urlpatterns = [ 
    path('', views.index, name='index'), 
    path('home/', views.home),
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
    path('getuserDos/', views.qryview, name='qryview'),
    path('showform/', views.showform, name='showForm'),
    path('getform', views.getform, name='getform'),
    path('dishes/<str:dish>', views.menuitems ),
    # re_path(r'^menu_item/([0-9]{2})/$', views.display_menu),
] 