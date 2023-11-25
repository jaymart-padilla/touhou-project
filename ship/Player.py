import pygame
from constants import window
from ship.Ship import Ship
from constants.ships import PLAYER_SPACE_SHIP
from constants.lasers import YELLOW_LASER

class Player(Ship):
  def __init__(self, x, y, width = 50, height = 50, health = 100, velocity = 5):
    super().__init__(x, y, width, height, health, velocity)
    self.ship_img = pygame.transform.scale(PLAYER_SPACE_SHIP, (width, height))
    self.laser_img = YELLOW_LASER
    self.mask = pygame.mask.from_surface(self.ship_img)
    self.max_health = health
  
  def draw(self, window):
    super().draw(window)
    if self.health >= 0:
      self.health_bar(window)
    
  def move_lasers(self, objs):
    self.cool_down()
    for laser in self.lasers:
      laser.move(-self.laser_velocity)
      if laser.off_screen(window.HEIGHT):
        self.lasers.remove(laser)
      else:
        # remove the laser and the object if it collides with an object
        for obj in objs:
          if laser.collision(obj):
            objs.remove(obj)
            if laser in self.lasers:
              self.lasers.remove(laser)
              
  def health_bar(self, window):
    pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + (self.ship_img.get_height() // 7), self.ship_img.get_width(), 5), border_radius=10)
    pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + (self.ship_img.get_height() // 7), self.ship_img.get_width() * (self.health / self.max_health), 5), border_radius=10)