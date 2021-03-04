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
        # Параметры снаряда
        self.bullet_speed = 1           # скорость снаряда
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)