import pygame, os
from constants.window import WIDTH, HEIGHT

# scale image to fit the window size
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'background-black.png')), (WIDTH, HEIGHT))
