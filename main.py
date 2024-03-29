import pygame
from pygame import Surface, Rect

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500

# Inicializar o módulo do pygame;
pygame.init()
print('setup start')

# Criação da Tela do Pygame
screen: Surface = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

# Carregar imagem e gerar uma superfície
fundo_surface = pygame.image.load('./assets/fundo.png').convert_alpha()
nave_surface = pygame.image.load('assets/nave.png').convert_alpha()

# Obter o retângulo da superfície;
fundo_rect: Rect = fundo_surface.get_rect(left=0, top=0)
nave_rect: Rect = nave_surface.get_rect(left=100, top=250)

# Desenhar na tela (screen)
screen.blit(source=fundo_surface, dest=fundo_rect)
screen.blit(source=nave_surface, dest=nave_rect)


# Atualizar a tela
pygame.display.flip()

print('setup end')

# Colocar um relógio no nosso jogo;
clock = pygame.time.Clock()

# Adicionado uma música ao jogo
pygame.mixer_music.load('./assets/fase1.mp3')
pygame.mixer_music.play(-1)
pygame.mixer_music.set_volume(0.3)

print('loop start')
while True:
  clock.tick(140)
  # print(f'{clock.get_fps() :.0f}')
  screen.blit(source=fundo_surface, dest=fundo_rect)
  screen.blit(source=nave_surface, dest=nave_rect)
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print('loop end')
      pygame.quit()
      quit()
  pressed_key = pygame.key.get_pressed()
  if pressed_key[pygame.K_w]:
    nave_rect.centery -= 1
  if pressed_key[pygame.K_s]:
    nave_rect.centery += 1
  if pressed_key[pygame.K_d]:
    nave_rect.centerx += 1
  if pressed_key[pygame.K_a]:
    nave_rect.centerx -= 1


