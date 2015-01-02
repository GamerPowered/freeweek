from django.shortcuts import render
from heroes import models as heroes_models
from lol import models as lol_models
from datetime import date

def home(request):
    heroes = heroes_models.FreeWeek.objects.filter(start__lte=date.today(),
                                    end__gte=date.today())

    lol = lol_models.FreeWeek.objects.filter(start__lte=date.today(),
                                    end__gte=date.today())

    context = {
        'heroes': heroes,
        'lol': lol,
    }

    return render(request, 'web/home.html', context)
