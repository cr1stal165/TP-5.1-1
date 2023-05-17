from django.shortcuts import render
import requests

def index(request):
    return render(request, 'index.html')

def all_topics(request):
    return render(request, 'all_topics.html')


def article_page(request, pk):
    return render(request, 'article_page.html')

