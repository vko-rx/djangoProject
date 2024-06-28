# BaseballMemoryApp/urls.py
from django.urls import path
from .views import game_create_view, game_list_view, calendar_view, check_date_view

urlpatterns = [
    path('create/', game_create_view, name='game_create'),
    path('', game_list_view, name='game_list'),
    path('calendar/', calendar_view, name='calendar'),
    path('check_date/', check_date_view, name='check_date'),
]
