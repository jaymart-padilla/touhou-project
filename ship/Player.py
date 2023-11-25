import pygame
from ship.Ship import Ship
from constants.ships import YELLOW_SPACE_SHIP
from constants.lasers import YELLOW_LASER

class Player(Ship):
  def __init__(self, x, y, width = 50, height = 50, health = 100, velocity = 5):
    super().__init__(x, y, width, height, health, velocity)
    self.ship_img = pygame.transform.scale(YELLOW_SPACE_SHIP, (width, height))
    self.laser_img = YELLOW_LASER
    self.mask = pygame.mask.from_surface(self.ship_img)
    self.max_health = health
  
  def draw(self, window):
    window.blit(self.ship_img, (self.x, self.y))