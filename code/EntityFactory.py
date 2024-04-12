import random

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT
from code.Fundo import Fundo
from code.Inimigo import Inimigo
from code.Jogador import Jogador


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                lista_bg = []
                for i in range(6):
                    lista_bg.append(Fundo(f'Level1Bg{i}', (0, 0)))
                    lista_bg.append(Fundo(f'Level1Bg{i}', (SCREEN_WIDTH, 0)))
                return lista_bg
            case 'Jogador1':
                return Jogador('Jogador1', (60, SCREEN_HEIGHT / 2 - 30))

            case 'Jogador2':
                return Jogador('Jogador2', (60, SCREEN_HEIGHT / 2 + 30))

            case 'Inimigo1':
                return Inimigo('Inimigo1', (SCREEN_WIDTH + 10, random.randint(0 + 40, SCREEN_HEIGHT - 40)))

            case 'Inimigo2':
                return Inimigo('Inimigo2', (SCREEN_WIDTH + 10, random.randint(0 + 40, SCREEN_HEIGHT - 40)))
