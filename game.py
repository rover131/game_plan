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
        print('hello')

    def run_game(self):
        """Запуск основного цикла игры"""
        print('qwer')
        while True:                                          # отслеживание клавиатуры и мышки
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.settings.color)            #назначаем цвет
            self.ship.blitime()
            pygame.display.flip()                            #обновление экрана


if __name__ == '__main__':
    ai = Initial()
    ai.run_game()
