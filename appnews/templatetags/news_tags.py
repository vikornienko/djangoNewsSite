from django import template

from appnews.models import Category

register = template.Library()

@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('appnews/list_categories.html')
def show_categories():
    categories = Category.objects.all()
    return {'categories': categories}