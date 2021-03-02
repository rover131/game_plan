import sys
import pygame
from settings import Settings
from ship import Ship


class Initial:
    def __init__(self):
        """Инициалируем игру"""
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode([self.settings.screen_width, self.settings.screen_height])
        pygame.display.set_caption("rover game")
        self.ship = Ship(self.screen)



    def run_game(self):
        """Запуск основного цикла игры"""
        print('qwer')
        while True:
            self._check_events()            # отслеживание клавиатуры и мышки
            self._update_screen()           # обновляем экран

    def _check_events(self):
        """Обработка событий клавиш"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:    # перемещаем направо
                    self.ship.rect.x += 10
                elif event.key == pygame.K_LEFT:   # перемещаем налево
                    self.ship.rect.x -= 10

    def _update_screen(self):
        self.screen.fill(self.settings.color)  # назначаем цвет
        self.ship.blitime()
        pygame.display.flip()


if __name__ == '__main__':
    ai = Initial()
    ai.run_game()
