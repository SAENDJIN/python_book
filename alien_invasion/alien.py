import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """"Клас, що представляє одного прибульця флоту"""

    def __init__(self, ai_game):
        """"Ініціалізувати прибульця та задати його початкове значення"""
        super().__init__()
        self.screen = ai_game.screen

        # Завантажити картинку прибульця та задати йому rect атрибут
        self.image = pygame.image.load('images/ufo.bmp')
        self.rect = self.image.get_rect()

        # Завантажувати кожного нового прибульця зверху зліва
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Зберігати прибульців в горизонтальному положенні
        self.x = float(self.rect.x)
