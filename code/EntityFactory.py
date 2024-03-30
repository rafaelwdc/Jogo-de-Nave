from code.Const import SCREEN_WIDTH
from code.Fundo import Fundo


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
