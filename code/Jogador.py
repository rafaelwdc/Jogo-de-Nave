import pygame

from code.Const import ENTITY_SPEED, SCREEN_HEIGHT, SCREEN_WIDTH, JOGADOR_KEY_UP, JOGADOR_KEY_DOWN, JOGADOR_KEY_RIGHT, \
    JOGADOR_KEY_LEFT
from code.Entity import Entity


class Jogador(Entity):
    def __init__(self, nome: str, position: tuple):
        super().__init__(nome, position)

    def move(self, ):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[JOGADOR_KEY_UP[self.nome]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.nome]
        if pressed_key[JOGADOR_KEY_DOWN[self.nome]] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.nome]
        if pressed_key[JOGADOR_KEY_LEFT[self.nome]] and self.rect.right < SCREEN_WIDTH:
            self.rect.centerx -= ENTITY_SPEED[self.nome]
        if pressed_key[JOGADOR_KEY_RIGHT[self.nome]] and self.rect.left > 0:
            self.rect.centerx += ENTITY_SPEED[self.nome]

