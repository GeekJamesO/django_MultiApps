# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    object = 'placeholder to display all the surveys created'
    print 'hello surveys: Index: ' + object
    context = { 'message' : object }
    return render(request, "surveys_app/index.html", context)

def new(request):
    object = 'placeholder for users to add a new survey'
    print 'hello surveys: New: ' + object
    context = { 'message' : object }
    return render(request, "surveys_app/index.html", context)
