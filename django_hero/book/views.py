from django.shortcuts import redirect, render
from django.views import generic

from .models import Page
from django.contrib.auth.decorators import login_required

from .forms import CharacterForm

@login_required
def index(request):
    title = 'Django Hero'
    subtitle = 'Django Hero is a book about Django'

    context = {
        'title': title,
        'subtitle': subtitle,
    }

    return render(request, 'index.html', context=context)

name = ''

@login_required
class PageView(generic.DetailView):
    model = Page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        global name
        context['name'] = name
        return context


def characterCreation(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            global name
            print('before', name)
            name = form.cleaned_data['name']
            print('after', name)
            return redirect('book:page', pk=2)
    else:
        form = CharacterForm()
    context = {
        'form': form,
    }
    return render(request, 'character_form.html', context)
    # return render(request, 'character_form.html')