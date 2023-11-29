import pygame
from utils.collide import collide
from constants.ships import ALIEN_SHIP, PURPLE_SHIP, BLUE_SHIP
from constants import misc_objects

class Power:
  POWER_UP_MAP = {
    "attack_speed": (ALIEN_SHIP),
    "add_laser": (PURPLE_SHIP),
    "movement_speed": (BLUE_SHIP),
    "regenerate_health": (misc_objects.HEART)
  }
  
  def __init__(self, x, y, power_type, width = 50, height = 50, velocity = 2.5):
      original_ship_img = self.POWER_UP_MAP[power_type]
      
      self.x = x
      self.y = y
      self.power_type = power_type
      self.width = width
      self.height = height
      self.velocity = velocity
      self.img = pygame.transform.scale(original_ship_img, (width, height))
      self.mask = pygame.mask.from_surface(self.img)
  
  def draw(self, window):
    window.blit(self.img, (self.x, self.y))

  def move(self):
    self.y += self.velocity

  def off_screen(self, height):
    return not(self.y <= height and self.y >= 0)
  
  def collision(self, obj):
    return collide(self, obj)