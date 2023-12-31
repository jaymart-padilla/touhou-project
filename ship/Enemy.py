import pygame
from ship.Ship import Ship
from constants.ships import ALIEN_SHIP
from constants.ships import PURPLE_SHIP
from constants.ships import BLUE_SHIP
from constants.lasers import RED_LASER
from constants.lasers import GREEN_LASER
from constants.lasers import PURPLE_LASER
from laser.Laser import Laser

class Enemy(Ship):
  COLOR_MAP = {
    "alien": (ALIEN_SHIP, RED_LASER, 10),
    "purple": (PURPLE_SHIP, GREEN_LASER, 20),
    "blue": (BLUE_SHIP, PURPLE_LASER, 30),
  }
  
  def __init__(self, x, y, color, width = 50, height = 50, health = 100, velocity = 5):
    super().__init__(x, y, width, height, health, velocity)
    original_ship_img, self.laser_img, self.health = self.COLOR_MAP[color]

    # Scale the ship's image to the specified width and height
    self.ship_img = pygame.transform.scale(original_ship_img, (width, height))
    self.mask = pygame.mask.from_surface(self.ship_img)
    self.max_health = self.health
  
  def shoot(self):
    if self.cool_down_counter == 0:
      laser = Laser(self.x + (self.width // 3), self.y, self.laser_img)
      self.lasers.append(laser)
      self.cool_down_counter = 1
  
  def move(self, velocity):
    self.y += velocity
    
  def draw(self, window):
    super().draw(window)
    if self.health >= 0:
      self.health_bar(window)
      
  def health_bar(self, window):
    pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + (self.ship_img.get_height() // 7), self.ship_img.get_width(), 5), border_radius=10)
    pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + (self.ship_img.get_height() // 7), self.ship_img.get_width() * (self.health / self.max_health), 5), border_radius=10)