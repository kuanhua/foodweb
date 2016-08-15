#-*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from django.contrib import auth

# Create your views here.

def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~' + request.GET['user_name'])
    else:
        return render_to_response('welcome.html', locals())

def use_session(request):
    request.session['lucky_number'] = 8
    if 'lucky_number' in request.session:
        lucky_number = request.session['lucky_number']
        response = HttpResponse('Your lucky_number is '+lucky_number)
    del request.session['lucky_number']
    return response

def session_test(request):
    sid = request.COOKIES['sessionid']
    sid2 = request.session.session_key
    s = Session.objects.get(pk=sid)
    s_info = 'Session ID:'+sid+\
             '<br>SessionID2:'+sid2+\
             '<br>Expire_date:'+str(s.expire_date)+\
             '<br>Data:'+str(s.get_decoded())
    return HttpResponse(s_info)

def login(request):
    if request.is_authenticated():
        return HttpResponseRedirect('/index/')

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = auth.authenticate(username=username, password=password)

    if user is not None and user.is_active:
        auth.login(request, user)
        return HttpResponseRedirect('/index/')
    else:
        return render_to_response('login.html', RequestContext(request, locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/index/')

def index(request):
    return render_to_response('index.html',RequestContext(request, locals()))
