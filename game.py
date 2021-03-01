import sys
import pygame


class Initial:
    """Класс для управлением ресурсами и поведением игры"""
    def __int__(self):
        """Инициализации игры """
        pygame.init()
        self.screen = pygame.display.set_mode([400, 300])
        pygame.display.set_caption("rover game")

    def run_game(self):
        """Запуск основного цикла программы"""
        while True:                               #отслеживание клавиатуры и мышки
            self.screen = pygame.display.set_mode([400, 300])
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                    pygame.quit()
            pygame.display.flip()                  #обновление экрана


if __name__ == '__main__':
    ai = Initial()
    ai.run_game()
