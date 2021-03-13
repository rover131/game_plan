class Settings:
    """Хранит все настройки игры"""

    def __init__(self):
        # Параметры экрана
        self.full_screen = True        # Полноэкранный режим
        self.screen_width = 800
        self.screen_height = 500
        self.color = (255, 255, 255)
        # Параметры  корабля
        self.speed_ship = 0.6             # СКОРОСТЬ корабля
        # Параметры снаряда
        self.bullet_speed = 0.5           # СКОРОСТЬ снаряда
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)    # цвет снаряда
        self.bullets_allowed = 100            # ОГРАНИЧЕНИЕ количества снарядов