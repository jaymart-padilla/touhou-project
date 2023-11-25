import pygame
from laser.Laser import Laser
from constants import window

class Ship:
    COOL_DOWN = 30
    
    def __init__(self, x, y, width = 50, height = 50, health = 100, velocity = 5):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.health = health
        self.velocity = velocity
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.laser_velocity = 5
        self.cool_down_counter = 0
        
    def draw(self, window):
      window.blit(self.ship_img, (self.x, self.y))
      for laser in self.lasers:
        laser.draw(window)
        
    def move_lasers(self, obj):
      self.cool_down()
      for laser in self.lasers:
        laser.move(self.laser_velocity)
        if laser.off_screen(window.HEIGHT):
          self.lasers.remove(laser)
        elif laser.collision(obj):
          obj.health -= 10
          self.lasers.remove(laser)
      
    def cool_down(self):
      # when cd_counter reaches 0, means the ship can shoot again
      # ship can only shoot when cd_counter reaches the self.COOL_DOWN
      if self.cool_down_counter >= self.COOL_DOWN:
        self.cool_down_counter = 0
      # runs the counter until the it reaches self.COOL_DOWN
      elif self.cool_down_counter > 0:
        self.cool_down_counter += 1

    def shoot(self):
      if self.cool_down_counter == 0:
        laser = Laser(self.x - (self.width // 6.25), self.y, self.laser_img)
        self.lasers.append(laser)
        self.cool_down_counter = 1
        