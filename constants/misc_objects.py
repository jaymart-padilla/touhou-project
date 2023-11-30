import pygame, os

# player lives
HEART_WIDTH = 15
HEART_HEIGHT = 15
HEART = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'heart.png')), (HEART_WIDTH, HEART_HEIGHT))

# power-ups
SPEED_UP = pygame.image.load(os.path.join('assets', 'speed-up.png'))
ADD_BULLET = pygame.image.load(os.path.join('assets', 'add-bullet.png'))
ATTACK_SPEED = pygame.image.load(os.path.join('assets', 'attack-speed.png'))