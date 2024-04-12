from code.Const import ENTITY_SPEED, SCREEN_WIDTH
from code.Entity import Entity


class Inimigo(Entity):
    def __init__(self, nome: str, position: tuple):
        super().__init__(nome, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.nome]
        if self.rect.right <= 0:
            self.rect.left = SCREEN_WIDTH
