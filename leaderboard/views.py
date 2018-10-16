from django.http import HttpResponse
from .models import Player, Matchlog, Ranks
from django.shortcuts import render
from .tables import PlayerTable
from django_tables2 import RequestConfig

def players(request):
	table = PlayerTable(Player.objects.all())
	RequestConfig(request).configure(table)
	return render(request, 'leaderboard/players.html', {'table': table})
