import pygame


class Ship:
    """Клас для керування кораблем"""

    def __init__(self, ai_game):
        """Ініціалізуємо корабель та задаємо йому початкову позицію"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Завантажити зображення корабля та отримати його rect
        self.image = pygame.image.load('images/706026.bmp')
        self.image_scale = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image_scale.get_rect()
        # Створювати кожен новий корабель внизу екрана, по центру
        self.rect.midbottom = self.screen_rect.midbottom
        # Індикатор руху
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Оновити поточну позицію корабля на основі індикаторів руху."""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

    def blitme(self):
        """Намалювати корабель у його поточному розташуванні"""
        self.screen.blit(self.image_scale, self.rect)
