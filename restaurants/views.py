#-*- coding: UTF-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
##from django.template.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from restaurants.models import Restaurant,  Comment
from restaurants.forms import CommentForm
from django.utils import timezone



# Create your views here.

def menu(request):
    if 'id' in request.GET and request.GET['id'] != '':
        restaurant = Restaurant.objects.get(id=request.GET['id'])
        return render_to_response('menu.html', locals())
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
    return render_to_response('restaurants_list.html', locals())

def comment(request,restaurant_id):

    if restaurant_id:
        r = Restaurant.objects.get(id=restaurant_id)
    else:
        return HttpResponseRedirect("/restaurants_list/")
    if request.POST:
        f = CommentForm(request.POST)
        if f.is_valid():
            visitor = request.POST['visitor']
            content = request.POST['content']
            email = request.POST['email']
            date_time = timezone.localtime(timezone.now())
            c = Comment.objects.create(
                visitor=visitor,
                email=email,
                content=content,
                date_time=date_time,
                restaurant=r
            )
            f = CommentForm(initial={'content':'沒意見'})
    else:
        f = CommentForm(initial={'content':'沒意見'})
    return render_to_response('comments.html',RequestContext(request,locals()))
'''
自行驗證方式
    errors = []
    if request.POST:
        visitor = request.POST['visitor']
        content = request.POST['content']
        email = request.POST['email']
        date_time = timezone.localtime(timezone.now())
        if any(not request.POST[k] for k in request.POST):
            errors.append('* 有空白欄位，請不要留空')
        if '@' not in email:
            errors.append('* email格式不正確，請重新輸入')
        if not errors:
            Comment.objects.create(visitor=visitor,email=email,content=content,date_time=date_time,restaurant=r)
            visitor,email,content=('','','')
'''



