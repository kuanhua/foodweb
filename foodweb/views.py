#-*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponse

# Create your views here.

def welcome(request):
    if 'user_name' in request.GET and request.GET['user_name'] != '':
        return HttpResponse('Welcome!~' + request.GET['user_name'])
    else:
        return render_to_response('welcome.html', locals())
