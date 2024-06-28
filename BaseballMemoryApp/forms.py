# BaseballMemoryApp/forms.py
from django import forms
from .models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['date', 'game', 'location', 'seat', 'result', 'image']  # 이미지 필드 포함
