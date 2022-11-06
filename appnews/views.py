from django.shortcuts import render, get_object_or_404, redirect

from .models import News, Category
from .forms import NewsForm

def index(request):

    news = News.objects.all()
    context_page = {
        'news': news,
        'title': 'News list'
    }
    return render(request, 'appnews/index.html', context_page)

def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)

    category = Category.objects.get(pk=category_id)
    context_page = {
        'news': news,
        'category': category
    }
    return render(request, 'appnews/category.html', context_page)

def get_one_news(request, news_id):
    one_news = get_object_or_404(News, pk=news_id)
    context_page = {'one_news': one_news}
    return render(request, 'appnews/view_news.html', context_page)

def add_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            News.objects.create(**form.cleaned_data)
            return redirect('home')
    else:
        form = NewsForm()
    context_page = {'form': form}
    return render(request, 'appnews/add_news.html', context_page)