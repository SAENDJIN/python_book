class Settings:
    """Клас для збереження всіх налаштувань гри"""

    def __init__(self):
        """Ініціалізувати налаштування гри"""
        # Screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (6, 18, 17)

        # Налаштування кулі
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colout = (250, 250, 250)
        self.bullet_allowed = 30

        # Налаштування прибульця
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        # fleet_direction 1 означає напрямок руху праворуч; -1 --ліворуч
        self.fleet_direction = 1

        # Налаштування корабля
        self.ship_speed = 5.5
        self.ship_limit = 3
