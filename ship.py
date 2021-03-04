import pygame
from settings import Settings


class Ship:
    """Класс, управляющий кораблем"""
    def __init__(self, ai_game):
        """Инициализация и задание начальной позиции"""
        self.settings = Settings()
        self.screen = ai_game
        self.screen_rect = ai_game.get_rect()               # размещение корабль в нужной позиции
        self.image = pygame.image.load('images/ship4.bmp')  # качаем картинку корабля
        self.rect = self.image.get_rect()                   # и получаем прямоугольник
        self.rect.midbottom = self.screen_rect.midbottom    # каждый корабль появляется у нижнего края экрана
        # Созданение координаты
        self.x = float(self.rect.x)
        # Флаги перемещения
        self.moving_right = False
        self.moving_left = False

    def update_poz(self):
        """Обновляем позицию корабля"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.speed_ship
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.speed_ship
        # Обновляем "прямоугольник" на новое положение
        self.rect.x = self.x

    def blitime(self):
        self.screen.blit(self.image, self.rect)             # рисуем корабль в текущей позиции