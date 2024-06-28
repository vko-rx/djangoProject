# BaseballMemoryApp/models.py
from django.db import models

class Game(models.Model):
    date = models.DateField()
    game = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    seat = models.CharField(max_length=100)
    result = models.CharField(max_length=100)
    image = models.ImageField(upload_to='game_images/', blank=True, null=True)  # 이미지 필드 추가

    def __str__(self):
        return f"{self.date} - {self.game}"
