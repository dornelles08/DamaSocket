import socket
from drawField import Dama
import pygame
from pygame.locals import *
import os

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Dama")
win.blit(pygame.image.load(os.path.join("imagens", "aguardandoAdversario.png")),(0,0))
pygame.display.update()