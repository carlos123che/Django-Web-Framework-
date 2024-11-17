"""
URL configuration for demo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import include, path

from luffy import views
from myapp import views

urlpatterns = [
    path('apptest/', include('apptest.urls')),
    path('pruebas/', include('pruebas.urls', namespace='pruebas')),
    path('admin/', admin.site.urls),
    path('say_hello/', views.say_hello),
    path('homepage/', views.homepage),
    path('display_date/', views.display_date),
    path('menu/', views.menu)
]

handler404 = 'demo.views.handler404'
