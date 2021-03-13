import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


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
        self.alien = pygame.sprite.Group()
        self._create_flot()

    def run_game(self):
        """Запуск основного цикла игры"""
        while True:
            self._check_events()            # отслеживание клавиатуры и мышки
            self.ship.update_poz()          # перемещаем корабль
            self.bullets.update()
            self._update_screen()           # обновляем экран
            self._update_buttles()          # удаление снарядов, вышедших за пределы окна
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)

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

    def _update_buttles(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _fire_bullet(self):
        """Создание нового снаряда и включение в группу bullets"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_flot(self):
        """создание флота"""
        alien = Alien(self)
        alien_width = alien.rect.width - 15 # ширина между прешельцами
        avail_space_x = self.settings.screen_width - (2 * alien_width)  # доступная ширина
        number_alien = avail_space_x // (2 * alien_width)
        # Создание первого ряда пришельцов
        for alien_number in range(number_alien):
            self._create_alien(alien_number, alien_width)

    def _create_alien(self, alien_number, alien_width):
        alien = Alien(self)
        alien.x = alien_width + 2 * alien_number * alien_width
        alien.rect.x = alien.x
        self.alien.add(alien)



    def _update_screen(self):
        self.screen.fill(self.settings.color)  # назначаем цвет
        self.ship.blitime()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.alien.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    ai = Initial()
    ai.run_game()
