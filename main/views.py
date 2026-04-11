from django.shortcuts import render, get_object_or_404

from main.models import Club, Transfer, Season, Player


def home_view(request):
    return render(request, 'index.html')


def clubs_view(request):
    clubs = Club.objects.all()

    country_query = request.GET.get('country')
    if country_query:
        clubs = clubs.filter(country__name=country_query)

    context = {
        'clubs': clubs,
    }
    return render(request, 'clubs.html', context)


def latest_transfers_view(request):
    tranfers = Transfer.objects.filter(
        season=Season.objects.last()
    ).order_by('-price')
    context = {
        'tranfers': tranfers
    }
    return render(request, 'latest-transfers.html', context)


def players_view(request):
    players = Player.objects.order_by('-price')
    context = {
        'players': players
    }
    return render(request, 'players.html', context)


def tryouts_view(request):
    return render(request, 'tryouts.html')


def u20_players_view(request):
    players = Player.objects.filter(age__lte=20).order_by('-price')
    context = {
        'players': players
    }
    return render(request, 'u-20.html', context)


def club_details_view(request, pk):
    club = get_object_or_404(Club, id=pk)
    players = Player.objects.filter(club=club).order_by('-price')
    context = {
        'club': club,
        'players': players
    }
    return render(request, 'club-details.html', context)
