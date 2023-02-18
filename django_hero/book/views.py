from django.shortcuts import render
from django.views import generic

from .models import Page
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    title = 'Django Hero'
    subtitle = 'Django Hero is a book about Django'

    context = {
        'title': title,
        'subtitle': subtitle,
    }

    return render(request, 'index.html', context=context)

@login_required
def page(request):
    title = 'Django Hero'
    subtitle = 'Django Hero is a book about Django'

    context = {
        'title': title,
        'subtitle': subtitle,
    }

    return render(request, 'page.html', context=context)

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