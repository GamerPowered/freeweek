from datetime import date
from django.shortcuts import render

from heroes.models import FreeWeek

def home(request):
    weeks = FreeWeek.objects.filter(start__lt=date.today(),
                                    end__gt=date.today())

    context = {
        'weeks': weeks,
    }

    return render(request, 'heroes/home.html', context)
