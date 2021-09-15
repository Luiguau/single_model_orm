from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import League, Team, Player

from . import team_maker

def index(request):
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")


def querylv1(request, q_id=1):
	context = {}
	if q_id ==1:
		context = {"t":"league","title": "1. All baseball leagues","items_list": League.objects.filter(sport="Baseball"),}
	elif q_id == 2:
		context = {"t":"league","title": "2. All womens' leagues","items_list": League.objects.filter(name__contains="women"),}
	elif q_id == 3:
		context = {"t":"league","title": "3. All leagues where sport is any type of hockey","items_list": League.objects.filter(sport__contains="hockey"),}
	elif q_id == 4:
		context = {"t":"league","title": "4. All leagues where sport is something OTHER THAN football","items_list": League.objects.exclude(sport__contains="football"),}
	elif q_id == 5:
		context = {"t":"league","title": "5. All leagues that call themselves 'conferences'","items_list": League.objects.filter(name__contains="conference"),}
	elif q_id == 6:
		context = {"t":"league","title": "6. All leagues in the Atlantic region","items_list": League.objects.filter(name__contains="atlantic"),}
	elif q_id == 7:
		context = {"t":"team","title": "7. All teams based in Dallas","items_list": Team.objects.filter(location="Dallas"),}
	elif q_id == 8:
		context = {"t":"team","title": "8. All teams named the Raptors","items_list": Team.objects.filter(team_name__contains="Raptor"),}
	elif q_id == 9:
		context = {"t":"team","title": "9. All teams whose location includes 'City'","items_list": Team.objects.filter(location__contains="city"),}
	elif q_id == 10:
		context = {"t":"team","title": "10. All teams whose names begin with 'T'","items_list": Team.objects.filter(team_name__startswith="T"),}
	elif q_id == 11:
		context = {"t":"team","title": "11. All teams, ordered alphabetically by location","items_list": Team.objects.all().order_by("location"),}
	elif q_id == 12:
		context = {"t":"team","title": "12. all teams, ordered by team name in reverse alphabetical order","items_list": Team.objects.all().order_by("-team_name"),}
	elif q_id == 13:
		context = {"t":"player","title": "13. Every player with last name 'Cooper'","items_list": Player.objects.filter(last_name="Cooper"),}
	elif q_id == 14:
		context = {"t":"player","title": "14. Every player with first name 'Joshua'","items_list": Player.objects.filter(first_name="Joshua"),}
	elif q_id == 15:
		context = {"t":"player","title": "15. Every player with last name 'Cooper' EXCEPT FOR Joshua","items_list": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),}
	elif q_id == 16:
		context = {"t":"player","title": "16. All players with first name 'Alexander' OR first name 'Wyatt'","items_list": Player.objects.filter(first_name__in=["Alexander","Wyatt"]),}
	
	return render(request, "leagues/index.html", context)


def querylv2(request, q_id=1):
	context = {}
	if q_id ==1:
		context = {"t":"league","title": "1. All baseball leagues","items_list": League.objects.filter(sport="Baseball"),}
	elif q_id == 2:
		context = {"t":"league","title": "2. All womens' leagues","items_list": League.objects.filter(name__contains="women"),}
	elif q_id == 3:
		context = {"t":"league","title": "3. All leagues where sport is any type of hockey","items_list": League.objects.filter(sport__contains="hockey"),}
	elif q_id == 4:
		context = {"t":"league","title": "4. All leagues where sport is something OTHER THAN football","items_list": League.objects.exclude(sport__contains="football"),}
	elif q_id == 5:
		context = {"t":"league","title": "5. All leagues that call themselves 'conferences'","items_list": League.objects.filter(name__contains="conference"),}
	elif q_id == 6:
		context = {"t":"league","title": "6. All leagues in the Atlantic region","items_list": League.objects.filter(name__contains="atlantic"),}
	elif q_id == 7:
		context = {"t":"team","title": "7. All teams based in Dallas","items_list": Team.objects.filter(location="Dallas"),}
	elif q_id == 8:
		context = {"t":"team","title": "8. All teams named the Raptors","items_list": Team.objects.filter(team_name__contains="Raptor"),}
	
	return render(request, "leagues/index.html", context)


def querylv3(request, q_id=1):
	context = {}
	if q_id ==1:
		context = {"t":"league","title": "1. All baseball leagues","items_list": League.objects.filter(sport="Baseball"),}
	elif q_id == 2:
		context = {"t":"league","title": "2. All womens' leagues","items_list": League.objects.filter(name__contains="women"),}
	elif q_id == 3:
		context = {"t":"league","title": "3. All leagues where sport is any type of hockey","items_list": League.objects.filter(sport__contains="hockey"),}
	elif q_id == 4:
		context = {"t":"league","title": "4. All leagues where sport is something OTHER THAN football","items_list": League.objects.exclude(sport__contains="football"),}
	elif q_id == 5:
		context = {"t":"league","title": "5. All leagues that call themselves 'conferences'","items_list": League.objects.filter(name__contains="conference"),}
	elif q_id == 6:
		context = {"t":"league","title": "6. All leagues in the Atlantic region","items_list": League.objects.filter(name__contains="atlantic"),}
	elif q_id == 7:
		context = {"t":"team","title": "7. All teams based in Dallas","items_list": Team.objects.filter(location="Dallas"),}
	
	return render(request, "leagues/index.html", context)
