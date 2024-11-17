from django.urls import path
from . import views

app_name = 'pruebas'
urlpatterns = [
    path('', views.index, name='index'),
]