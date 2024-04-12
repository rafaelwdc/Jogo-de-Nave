import random
import sys

import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import COLOR_YELLOW, MENU_OPTION, EVENT_INIMIGO
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, screen, name, menu_option):
        self.screen: Surface = screen
        self.name = name
        self.mode = menu_option
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Jogador1'))
        if menu_option in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Jogador2'))
        pygame.time.set_timer(EVENT_INIMIGO, 4000)



    def run(self):
        pygame.mixer_music.load(f'./assets/levels/Level1/{self.name}.mp3')
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.screen.blit(source=ent.surf, dest=ent.rect)
                self.level_text(14, f'FPS: {clock.get_fps():.0f}', COLOR_YELLOW, (25, 16))
                ent.move()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print('Fechou')
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_INIMIGO:
                    escolha = random.choice(('Inimigo1', 'Inimigo2'))
                    self.entity_list.append(EntityFactory.get_entity(escolha))
            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_position: tuple):
        text_font: Font = pygame.font.Font("./assets/audiowire_font.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_position[0], top=text_position[1])
        self.screen.blit(source=text_surf, dest=text_rect)
