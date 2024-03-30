import sys

# Importando Pacotes do Pygame
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

# Importando as Constantes
from code.Const import SCREEN_WIDTH, COLOR_YELLOW, MENU_OPTION, COLOR_WHITE, COLOR_ORANGE


# Criando a Classe
class Menu:
    # Inicializa a Classe criando uma tela
    def __init__(self, screen):
        self.screen: Surface = screen
        self.surf = pygame.image.load('./assets/fundo.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        # Seleciona e Executa a Musica
        # pygame.mixer_music.load('./assets/fase1.mp3')
        # pygame.mixer_music.play(-1)

        # Opção Default do Menu
        menu_option = 0

        # Escreve as opções na tela
        while True:
            self.screen.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "spaceship", COLOR_YELLOW, ((SCREEN_WIDTH / 2), 70))
            self.menu_text(65, "STRIKE", COLOR_YELLOW, ((SCREEN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], COLOR_ORANGE, ((SCREEN_WIDTH / 2), 350 + 30 * i))
                else:
                    self.menu_text(25, MENU_OPTION[i], COLOR_WHITE, ((SCREEN_WIDTH / 2), 350 + 30 * i))
            pygame.display.flip()

            # Verifica qual dos eventos foi disparado
            for event in pygame.event.get():

                # Dispara o Evento de Fechar o Jogo
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # Dispara o Evento de Clicar uma Tecla
                if event.type == pygame.KEYDOWN:
                    # Dispara o Evento da Tecla para Baixo para escolher outra opção no menu
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    # Dispara o Evento da Tecla para Cima para escolher outra opção no menu
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    # Dispara o Evento da Tecla para Enter para selecionar uma opção do menu
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_position: tuple):
        text_font: Font = pygame.font.Font("./assets/audiowire_font.ttf", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color)
        text_rect: Rect = text_surf.get_rect(center=text_center_position)
        self.screen.blit(source=text_surf, dest=text_rect)
