from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Category


# responsible for the main page view
def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}

    return render(request, 'rango/index.html', context=context_dict)


def about(request):
    context_dict = {'aboutmessage': "This tutorial has been put together by k"}
    return render(request, 'rango/about.html', context=context_dict)

