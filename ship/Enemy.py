import pygame
from ship.Ship import Ship
from constants.ships import ALIEN_SHIP
from constants.ships import PURPLE_SHIP
from constants.ships import BLUE_SHIP
from constants.lasers import RED_LASER
from constants.lasers import GREEN_LASER
from constants.lasers import BLUE_LASER
from laser.Laser import Laser

class Enemy(Ship):
  COLOR_MAP = {
    "red": (ALIEN_SHIP, RED_LASER),
    "green": (PURPLE_SHIP, GREEN_LASER),
    "blue": (BLUE_SHIP, BLUE_LASER),
  }
  
  def __init__(self, x, y, color, width = 50, height = 50,  health = 100, velocity = 5):
    super().__init__(x, y, width, height, health, velocity)
    original_ship_img, self.laser_img = self.COLOR_MAP[color]

    # Scale the ship's image to the specified width and height
    self.ship_img = pygame.transform.scale(original_ship_img, (width, height))
    self.mask = pygame.mask.from_surface(self.ship_img)
  
  def shoot(self):
    if self.cool_down_counter == 0:
      laser = Laser(self.x - 15, self.y, self.laser_img)
      self.lasers.append(laser)
      self.cool_down_counter = 1
  
  def move(self, velocity):
    self.y += velocity