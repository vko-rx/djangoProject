# BaseballMemoryApp/views.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import GameForm
from .models import Game


def game_create_view(request):
    initial_data = {}
    if request.method == 'GET' and 'date' in request.GET:
        initial_data['date'] = request.GET['date']

    if request.method == 'POST':
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calendar')
    else:
        form = GameForm(initial=initial_data)
    return render(request, 'game_create.html', {'form': form})


def game_list_view(request):
    date = request.GET.get('date')
    if date:
        games = Game.objects.filter(date=date)
    else:
        games = Game.objects.all()
    return render(request, 'game_list.html', {'games': games})


def calendar_view(request):
    return render(request, 'calendar.html')


def check_date_view(request):
    date = request.GET.get('date')
    if date:
        games = Game.objects.filter(date=date)
        if games.exists():
            return JsonResponse({'exists': True})
    return JsonResponse({'exists': False})
