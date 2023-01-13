from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.urls import reverse

from .models import Player, Team


def index(request):
    return HttpResponse(request, "league/index.html")


def player_view(request, player_id: int):
    """Display the profile of a player given the PK"""

    player = get_object_or_404(Player, pk=player_id)
    return render(request, "league/index.html", {"player": player})


def team_view(request, team_name: str):
    """Display the profile of a team given the PK"""

    team = get_object_or_404(Team, pk=team_name)
    return render(request, "league/team.html", {"team": team})
