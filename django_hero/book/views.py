from django.shortcuts import render
from django.views import generic

from .models import Page

def index(request):
    title = 'Django Hero'
    subtitle = 'Django Hero is a book about Django'

    context = {
        'title': title,
        'subtitle': subtitle,
    }

    return render(request, 'index.html', context=context)

class PageView(generic.DetailView):
    model = Page

def characterForm(request):
    title = 'Django Hero'
    subtitle = 'Django Hero is a book about Django'

    context = {
        'title': title,
        'subtitle': subtitle,
    }

    return render(request, 'character_form.html', context=context)

def login(request):
    title = 'Django Hero'
    subtitle = 'Django Hero is a book about Django'

    context = {
        'title': title,
        'subtitle': subtitle,
    }

    return render(request, 'login.html', context=context)

def register(request):
    title = 'Django Hero'
    subtitle = 'Django Hero is a book about Django'

    context = {
        'title': title,
        'subtitle': subtitle,
    }

    return render(request, 'register.html', context=context)