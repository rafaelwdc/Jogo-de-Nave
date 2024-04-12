# C
import pygame

COLOR_YELLOW = (255, 242, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_ORANGE = (255, 128, 0)

# E
ENTITY_SPEED = {'Level1Bg0': 0,
                'Level1Bg1': 2,
                'Level1Bg2': 3,
                'Level1Bg3': 4,
                'Level1Bg4': 5,
                'Level1Bg5': 6,
                'Jogador1': 3,
                'Jogador2': 3,
                'Inimigo1': 2,
                'Inimigo2': 1
                }
EVENT_INIMIGO = pygame.USEREVENT + 1

# J
JOGADOR_KEY_UP = {'Jogador1': pygame.K_UP,
                  'Jogador2': pygame.K_w,
                  }

JOGADOR_KEY_DOWN = {'Jogador1': pygame.K_DOWN,
                    'Jogador2': pygame.K_s
                    }

JOGADOR_KEY_RIGHT = {'Jogador1': pygame.K_RIGHT,
                     'Jogador2': pygame.K_d
                     }

JOGADOR_KEY_LEFT = {'Jogador1': pygame.K_LEFT,
                    'Jogador2': pygame.K_a
                    }

# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOP',
               'NEW GAME 2P - RANK',
               'EXIT')

# S
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 499
