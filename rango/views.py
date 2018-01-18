from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category
from rango.models import Page


def show_category(request, category_name_slug):
    # a context dictionary which can pass to the template rendering engine
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        # add our results list to the template context under name pages
        context_dict['pages'] = pages

        context_dict['category'] = category

    except Category.DoesNotExist:
        # the template will display 'no category' message for us
        context_dict['pages'] = None
        context_dict['category'] = None
    return render(request, 'rango/category.html', context_dict)


# responsible for the main page view
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'aboutmessage': "This tutorial has been put together by k"}
    return render(request, 'rango/about.html', context=context_dict)

