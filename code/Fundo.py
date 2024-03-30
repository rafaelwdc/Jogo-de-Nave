from code.Const import SCREEN_WIDTH, ENTITY_SPEED
from code.Entity import Entity


class Fundo(Entity):
    def __init__(self, nome: str, position: tuple):
        super().__init__(nome, position)

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.nome]
        if self.rect.right <= 0:
            self.rect.left = SCREEN_WIDTH

