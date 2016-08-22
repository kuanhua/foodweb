#-*- coding: UTF-8 -*-
from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~' + request.GET['user_name'])
    else:
#        return render_to_response('welcome.html', locals())
        return render(request, 'welcome.html')

def use_session(request):
    request.session['lucky_number'] = 8
    if 'lucky_number' in request.session:
        lucky_number = request.session['lucky_number']
        response = HttpResponse('Your lucky_number is '+lucky_number)
    del request.session['lucky_number']
    return response

def session_test(request):
    sid = request.COOKIES['sessionid']  # session依附cookie
    sid2 = request.session.session_key  # 純 session
    s = Session.objects.get(pk=sid)
    s_info = 'Session ID:'+sid+\
             '<br>SessionID2:'+sid2+\
             '<br>Expire_date:'+str(s.expire_date)+\
             '<br>Data:'+str(s.get_decoded())
    return HttpResponse(s_info)

def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html', RequestContext(request, locals()))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def index(request):
    return render_to_response('index.html',RequestContext(request, locals()))

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return HttpResponseRedirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render_to_response('register.html',RequestContext(request,locals()))

def test(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~' + request.GET['user_name'])
    else:
#        return render_to_response('welcome.html', locals())
        return render(request, 'test.html')

@login_required
def list_users(request):
    users = auth.models.User.objects.all()
    return render(request, 'users_list.html', locals())