from django.shortcuts import render

from main.models import Club


def home_view(request):
    return render(request, 'index.html')


def clubs_view(request):
    context = {
        'clubs': Club.objects.all()
    }
    return render(request, 'clubs.html', context)
