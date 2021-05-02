from django.shortcuts import render
from django.contrib import admin
from django.urls import path,include
from store.views.home import Index
from django.db import models




def search(request):
    query=request.GET['query']
    allPosts= models.filter(title__icontains=query)
    params={'allPosts': allPosts}
    return render(request, '/search.html', params)