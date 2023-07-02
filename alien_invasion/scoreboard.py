import pygame.font


class Scoreboard:
    """Клас, що виводить рахунок."""

    def __init__(self, ai_game):
        """Ініціалізація атрибутів, пов'язаних із рахунком."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # Налаштування шрифту для відображення рахунку
        self.text_color = (57, 74, 45)
        self.font = pygame.font.SysFont("Pixeloid Sans", 48)

        # Підготувати зображення з початковим рахуном.
        self.prep_score()

    def prep_score(self):
        """"Перетворити рахунок на зображення"""
        score_str = str(self.stats.score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        # Показати рахунок у верхньому правому куті екрану.
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """"Показати рахунок на екрані."""
        self.screen.blit(self.score_image, self.score_rect)