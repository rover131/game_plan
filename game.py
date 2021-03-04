import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet


class Initial:
    def __init__(self):
        """Инициалируем игру"""
        pygame.init()
        self.settings = Settings()
        if self.settings.full_screen:
            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
            self.settings.screen_width = self.screen.get_rect().width
            self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode([self.settings.screen_width, self.settings.screen_height])
        pygame.display.set_caption("rover game")
        self.ship = Ship(self.screen)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()            # отслеживание клавиатуры и мышки
            self.ship.update_poz()          # перемещаем корабль
            self.bullets.update()
            self._update_screen()           # обновляем экран

    def _check_events(self):
        """Обработка событий клавиш"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_up_events(event)

    def _check_down_events(self, event):
        """Реакция на нажатие клавиш"""
        if event.key == pygame.K_RIGHT:  # перемещаем направо вкл
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:  # перемещаем налево вкл
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_up_events(self, event):
        """Реакция на отпуснаие клавиш"""
        if event.key == pygame.K_RIGHT:  # перемещаем направо выкл
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:  # перемещаем налево выкл
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Создание нового снаряда и включение в группу bullets"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_screen(self):
        self.screen.fill(self.settings.color)  # назначаем цвет
        self.ship.blitime()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        pygame.display.flip()


if __name__ == '__main__':
    ai = Initial()
    ai.run_game()
