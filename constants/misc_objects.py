import pygame, os

# player lives
HEART_WIDTH = 15
HEART_HEIGHT = 15
HEART = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'heart.png')), (HEART_WIDTH, HEART_HEIGHT))

