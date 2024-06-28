# BaseballMemoryApp/models.py
from django.db import models

class Game(models.Model):
    date = models.DateField()
    game = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    seat = models.CharField(max_length=100)
    result = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.date} - {self.game}"
