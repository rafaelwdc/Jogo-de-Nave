#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface
from pygame.font import Font

from code.Const import SCREEN_WIDTH, SCREEN_HEIGHT
from code.Menu import Menu


class Jogo:
  def __init__(self):
    pygame.init()
    self.screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

  def run(self):
    while True:
      menu = Menu(self.screen)
      menu.run()

