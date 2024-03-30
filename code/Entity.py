from abc import ABC, abstractmethod

import pygame.image


class Entity(ABC):
    def __init__(self, nome: str, position: tuple):
        self.nome = nome
        self.surf = pygame.image.load('./assets/levels/level_1/' + nome + '.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self):
        pass
