import pygame
from ship.Ship import Ship
from constants.ships import RED_SPACE_SHIP
from constants.ships import GREEN_SPACE_SHIP
from constants.ships import BLUE_SPACE_SHIP
from constants.lasers import RED_LASER
from constants.lasers import GREEN_LASER
from constants.lasers import BLUE_LASER
from laser.Laser import Laser

class Enemy(Ship):
  COLOR_MAP = {
    "red": (RED_SPACE_SHIP, RED_LASER),
    "green": (GREEN_SPACE_SHIP, GREEN_LASER),
    "blue": (BLUE_SPACE_SHIP, BLUE_LASER),
  }
  
  def __init__(self, x, y, color, width = 50, height = 50,  health = 100, velocity = 5):
    super().__init__(x, y, width, height, health, velocity)
    self.ship_img, self.laser_img = self.COLOR_MAP[color]
    self.mask = pygame.mask.from_surface(self.ship_img)
  
  def shoot(self):
    if self.cool_down_counter == 0:
      laser = Laser(self.x - 15, self.y, self.laser_img)
      self.lasers.append(laser)
      self.cool_down_counter = 1
  
  def move(self, velocity):
    self.y += velocity