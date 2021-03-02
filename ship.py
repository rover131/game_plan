import pygame


class Ship:
    """Класс, управляющий кораблем"""
    def __init__(self, ai_game):
        """Инициализация и задание начальной позиции"""
        self.screen = ai_game
        self.screen_rect = ai_game.get_rect()               #размещение корабль в нужной позиции
        self.image = pygame.image.load('images/ship4.bmp')  #качаем картинку корабля
        self.rect = self.image.get_rect()                   #и получаем прямоугольник
        self.rect.midbottom = self.screen_rect.midbottom    #каждый корабль появляется у нижнего края экрана

    def blitime(self):
        self.screen.blit(self.image, self.rect)             #рисуем корабль в текущей позиции