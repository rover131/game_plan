class Settings:
    """Хранит все настройки игры"""

    def __init__(self):
                    # Параметры экрана
        self.full_screen = True        # Полноэкранный режим
        self.screen_width = 800
        self.screen_height = 300
        self.color = (255, 255, 255)
        # Скорость корабля
        self.speed_ship = 1
