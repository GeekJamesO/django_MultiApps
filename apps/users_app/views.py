# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

# /register - display 'placeholder for users to create a new user record'
def register(request):
    print 'hello users:register'
    object = 'placeholder for users to create a new user record'
    context = { 'message': object }
    return render(request, "users_app/register.html", context)

# /login - display 'placeholder for users to login'
def login(request):
    print 'hello users:login'
    object = 'placeholder for users to login'
    context = { 'message': object }
    return render(request, "users_app/login.html", context)

# /users/new - have the same method that handles /register also handle the url
# request of /users/new
def newUser(request):
    print 'hello users:newUser'
    return register(request)

# /users - display 'placeholder to later display all the list of users'
def users(request):
    print 'hello users:users'
    object = 'placeholder to later display all the list of users'
    context = { 'message': object }
    return render(request, "users_app/users.html", context)
