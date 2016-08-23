#-*- coding: UTF-8 -*-
"""foodweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.views import login, logout
# from views import index, welcome, register
# from restaurants.views import menu, list_restaurants, comment
from django.conf import settings
import django.contrib.auth.views
import views
import restaurants.views

from django.views.generic.base import TemplateView

admin.autodiscover()

urlpatterns = [
    url(r'^admin/',             include(admin.site.urls)),
    url(r'^menu/(?P<pk>\d+)/',  login_required(restaurants.views.MenuView.as_view())),
    url(r'^restaurants_list/',  login_required(restaurants.views.RestaurantsView.as_view())),
    url(r'^comment/(\d{1,5})/', login_required(restaurants.views.comment)),
    url(r'^login/',             django.contrib.auth.views.login),
    url(r'^logout/',            django.contrib.auth.views.logout),
    url(r'^accounts/login/',    django.contrib.auth.views.login),
    url(r'^accounts/logout/',   django.contrib.auth.views.logout),
    url(r'^index/',             TemplateView.as_view(template_name='index.html')),
    url(r'^welcome/',           views.welcome),
    url(r'^accounts/register/', views.register),
    url(r'^users_list/',         views.list_users),
]
# url(r'^index/',             views.index),
# url(r'index/',              views.IndexView.as_view()),
# url(r'^index/',              TemplateView().as_view(template_name='index.html')),
# url(r'^restaurants_list/',  login_required(restaurants.views.list_restaurants)),
# url(r'^menu/',              login_required(restaurants.views.menu)),
if settings.DEBUG:
    urlpatterns += [
        url(r'^test/', views.test),
    ]
