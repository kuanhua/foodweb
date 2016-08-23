#-*- coding: UTF-8 -*-
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from restaurants.models import Restaurant,  Comment
from restaurants.forms import CommentForm
from django.utils import timezone
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required, permission_required

from django.views.generic.list import ListView
from django.utils.decorators import method_decorator

from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView

# Create your views here.

class MenuView(DetailView):
    model = Restaurant
    template_name = 'menu.html'
    context_object_name = 'restaurant'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(MenuView, self).dispatch(request, *args, **kwargs)

'''
def menu(request):
    if 'id' in request.GET and request.GET['id'] != '':
        restaurant = Restaurant.objects.get(id=request.GET['id'])
        return render_to_response('menu.html', locals())
    else:
        return HttpResponseRedirect("/restaurants_list")
'''

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

'''
@login_required
def list_restaurants(request):
#    if not request.user.is_authenticated():
##        return HttpResponseRedirect('/index/')
#        return HttpResponseRedirect('/accounts/login/?next={0}'.format(request.path))
    restaurants = Restaurant.objects.all()
    request.session['restaurants'] = restaurants
    return render_to_response('restaurants_list.html', locals())
'''

class RestaurantsView(ListView):
    model = Restaurant
    template_name = 'restaurants_list.html'
    context_object_name = 'restaurants'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(RestaurantsView, self).dispatch(request, *args, **kwargs)

'''
@permission_required('restaurants.can_comment',)
def comment(request, restaurant_id):

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
            f = CommentForm(initial={'content':'很美味'})
    else:
        f = CommentForm(initial={'content':'很美味'})
    return render_to_response('comments.html',RequestContext(request, locals()))
'''

class CommentView(FormView):
    form_class = CommentForm
    template_name = 'comments.html'
    success_url = '/comment'
    initial = {'content':u'很美味'}

    def form_valid(self, form):
        Comment.objects.create(
            visitor = form.cleaned_data['visitor'],
            email = form.cleaned_data['email'],
            content = form.cleaned_data['content'],
            date_time = timezone.localtime(timezone.now()),
            restaurant = Restaurant.objects
        )





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



