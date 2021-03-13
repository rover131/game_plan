import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """класс предоставляющий одного пришельца"""
    def __init__(self, ai_game):
        super().__init__()                  # правильная реализация наследования от класса super
        self.screen = ai_game.screen
        # загрузка изображения и преобразование его в прямоугольник
        self.image = pygame.image.load('images/Prih2.jpg')
        self.rect = self.image.get_rect()
        # появление пришельца в верхнем левом углу
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # сохранение позиции
        self.x = float(self.rect.x)
