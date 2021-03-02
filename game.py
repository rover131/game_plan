import sys
import pygame


class Initial:
    def __init__(self):
        """Инициалируем игру"""
        pygame.init()
        self.screen = pygame.display.set_mode([800, 400])
        pygame.display.set_caption("rover game")
        self.color = (230, 230, 230)        #назначаем цвет
        print('hello')

    def run_game(self):
        """Запуск основного цикла игры"""
        print('qwer')
        while True:       # отслеживание клавиатуры и мышки
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            self.screen.fill(self.color)
            pygame.display.flip()           #обновление экрана


if __name__ == '__main__':
    asd = Initial()
    asd.run_game()
