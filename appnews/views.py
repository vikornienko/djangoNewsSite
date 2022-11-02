from django.shortcuts import render

from .models import News

def index(request):
    news = News.objects.all()
    context_page = {'news': news, 'title': 'News list'}
    return render(request, 'appnews/index.html', context_page)

