"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.urls import re_path
from hello import views

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^about/contacts', views.contacts, name='contacts'),
    re_path(r'^about', views.about, name='about'),

    # re_path(r'^products/(?P<productid>\d+)/', views.products),
    # re_path(r'^users/(?P<id>\d+)/(?P<name>\D+)', views.users),
    path('products/<int:productid>/', views.products),
    path('users/<int:id>/<name>', views.users),

    path('queryparams/<int:productid>/', views.queryparams),


    re_path(r'^news/', views.news),
    re_path(r'^details/', views.details),


    # path('contacts', views.contacts, name='contacts'),
    path('admin/', admin.site.urls),
]
