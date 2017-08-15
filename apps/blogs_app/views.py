# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

# /blogs - display "placeholder to later display all the list of blogs" via
# HttpResponse. Have this be handled by a method named 'index'.
def index(request):
    print 'hello blogs:index'
    print strftime("%Y-%m-%d %H:%M:%S", gmtime())
    print get_random_string(length=14)

    context = {  }
    return render(request, "blogs_app/index.html", context)

# /blogs/new - display "placeholder to display a new form to create a new blog"
# via HttpResponse. Have this be handled by a method named 'new'.
def new(request):
    print 'hello blogs:new'
    context = {  }
    return render(request, "blogs_app/new.html", context)

# /blogs/create - Have this be handled by a method named 'create'.  For now, have
# this url redirect to /blogs.
def create(request):
    if request.method == "POST":
        print "*"*50
        print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
        print "*"*50
        return redirect("/")
    else:
        return redirect("/")

# /blogs/{{number}} - display 'placeholder to display blog {{number}}.
# For example /blogs/15 should display a message 'placeholder to display blog 15'.
# Have this be handled by a method named 'show'.
def show(request, number):
    print 'hello blogs:show'
    context = { 'number': number }
    return render(request, "blogs_app/show.html", context)

# /blogs/{{number}}/edit - display 'placeholder to edit blog {{number}}.
# Have this be handled by a method named 'edit'.
def edit(request, number):
    print 'hello blogs:edit'
    context = { 'number': number }
    return render(request, "blogs_app/edit.html", context)

# /blogs/{{number}}/delete - Have this be handled by a method named 'destroy'.
# For now, have this url redirect to /blogs.
def destroy(request, number):
    # print 'hello blogs:destroy'
    context = { 'number': number }
    return index(request)
