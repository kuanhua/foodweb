#-*- coding: UTF-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import HttpResponseRedirect
from restaurants.models import Restaurant
from django.utils import timezone



# Create your views here.

def menu(request):
    if 'id' in request.GET and request.GET['id'] != '':
        restaurant = Restaurant.objects.get(id=request.GET['id'])
        return render_to_response('menu.html', RequestContext(request, locals()))
    else:
        return HttpResponseRedirect("/restaurants_list")


'''
方法2,3用此 method
def menu(request,id):
#    path = request.path
#   restaurants = Restaurant.objects.all()
    if id:
        restaurant = Restaurant.objects.get(id=id)
        return render_to_response('menu.html', locals())
    else:
        return HttpResponseRedirect("/restaurants_list")
'''
def list_restaurants(request):
    restaurants = Restaurant.objects.all()
    return render_to_response('restaurants_list.html', RequestContext(request, locals()))

def comment(request,restaurant_id):
    if restaurant_id:
        r = Restaurant.objects.get(id=restaurant_id)
    else:
        return HttpResponseRedirect("/restaurants_list")
    if request.POST:
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        date_time = timezone.localtime(timezone.now())
        Comment.objects.create(visitor=visitor,email=email,content=content,date_time=date_time,restaurant=r)
##  return render_to_response('comments.html',locals())
    return render_to_response('comments.html', RequestContext(request, locals()))