from django.urls import path

from .views import index, get_category, get_one_news, add_news

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', get_one_news, name='view_news'),
    path('news/add-news/', add_news, name='add_news'),
]