from django.shortcuts import render

def index(request):
    title = 'Django Hero'
    subtitle = 'Django Hero is a book about Django'

    context = {
        'title': title,
        'subtitle': subtitle,
    }

    return render(request, 'index.html', context=context)

def page(request):
    title = 'Django Hero'
    subtitle = 'Django Hero is a book about Django'

    context = {
        'title': title,
        'subtitle': subtitle,
    }

    return render(request, 'page.html', context=context)

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