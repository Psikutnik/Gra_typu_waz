"""
Package główny gry Snake.

Zawiera wszystkie moduły niezbędne do działania gry:
- game.py - główna logika gry
- snake.py - implementacja węża
- food.py - implementacja jedzenia
- high_scores.py - zarządzanie wynikami
"""

from .game import Game
from .snake import Snake
from .food import Food
from .high_scores import HighScores

__all__ = ['Game', 'Snake', 'Food', 'HighScores']