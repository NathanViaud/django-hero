from django.shortcuts import redirect, render
from django.views import generic

from .models import Game, Page
from django.contrib.auth.decorators import login_required

from .forms import CharacterForm

@login_required
def index(request):
    title = 'Django Hero'
    subtitle = 'Django Hero is a book about Django'

    try:
        req = Game.objects.get(user=request.user)
    except Game.DoesNotExist:
        req = None

    context = {
        'title': title,
        'subtitle': subtitle,
        'game': req,
    }

    return render(request, 'index.html', context=context)

name = ''

class PageView(generic.DetailView):
    model = Page
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        global name
        context['name'] = name
        if(name == ''):
            try:
                req = Game.objects.get(user=self.request.user)
            except Game.DoesNotExist:
                req = None
            if req:
                context['name'] = req.name
                name = req.name
        if(name != ''):
            Game.objects.filter(user=self.request.user).update(pageNumber=self.kwargs['pk'])
        return context


def characterCreation(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST)
        if form.is_valid():
            global name
            name = form.cleaned_data['name']
            if(request.user.is_authenticated and name != ''):
                try:
                    game = Game.objects.get(user=request.user)
                    game.name = name
                    game.pageNumber = 2
                    game.save()
                except Game.DoesNotExist:
                    Game.objects.create(name=name, pageNumber=2, user=request.user)
            return redirect('book:page', pk=27)
    else:
        form = CharacterForm()
    context = {
        'form': form,
    }
    return render(request, 'character_form.html', context)