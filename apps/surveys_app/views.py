# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    object = 'placeholder to display all the surveys created'
    context = { 'message' : object }
    return render(request, "surveys_app/index.html", context)

def new(request):
    object = 'placeholder for users to add a new survey'
    context = { 'message' : object }
    return render(request, "surveys_app/index.html", context)

def create(request):
    return redirect('/surveys')

def show(request, survey_id):
    return HttpResponse("placeholder to display survey {}".format(survey_id))

def edit(request, survey_id):
    return HttpResponse("placeholder to edit survey {}".format(survey_id))

def delete(request, survey_id):
    return redirect('/surveys')
