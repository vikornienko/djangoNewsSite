from django.shortcuts import render

from .models import News, Category

def index(request):
    categories = Category.objects.all()
    news = News.objects.all()
    context_page = {
        'categories': categories,
        'news': news,
        'title': 'News list'
    }
    return render(request, 'appnews/index.html', context_page)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context_page = {
        'news': news,
        'categories': categories,
        'category': category
    }
    return render(request, 'appnews/category.html', context_page)

