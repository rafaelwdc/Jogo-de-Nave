import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import SCREEN_WIDTH


class Menu:
    def __init__(self, screen):
        self.screen: Surface = screen
        self.surf = pygame.image.load('./assets/fundo.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./assets/fase1.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "SPACE", (255, 242, 0), ((SCREEN_WIDTH / 2), 70))
            self.menu_text(50, "shooter", (255, 242, 0), ((SCREEN_WIDTH / 2), 70))
            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.screen.blit(source=text_surf, dest=text_rect)
