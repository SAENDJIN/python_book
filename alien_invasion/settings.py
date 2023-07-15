class Settings:
    """Клас для збереження всіх налаштувань гри"""

    def __init__(self):
        """Ініціалізувати постійні налаштування гри"""
        # Screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (6, 18, 17)

        # Налаштування кулі
        self.bullet_speed = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colout = (250, 250, 250)
        self.bullet_allowed = 15

        # Налаштування прибульця
        self.alien_speed = 1.0
        self.fleet_drop_speed = 100
        # fleet_direction 1 означає напрямок руху праворуч; -1 --ліворуч
        self.fleet_direction = 1

        # Налаштування корабля
        self.ship_speed = 5.5
        self.ship_limit = 3

        # Як швидко гра має прискорюватись
        self.speedup_scale = 1.2

        # Як швидко збільшується вартість прибульців
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Ініціалізація змінних налаштувань"""
        self.ship_speed = 5.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction 1 представляє напрямок праворуч; -1 -- ліворуч.
        self.fleet_direction = 1

        # Отримання балів
        self.alien_points = 50

    def increase_speed(self):
        """Збільшення налаштувань швидкості та вартості прибульців"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
