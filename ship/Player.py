import pygame, random
from constants.window import HEIGHT
from ship.Ship import Ship
from constants.ships import PLAYER_SPACE_SHIP
from constants.lasers import YELLOW_LASER
from powerup.Power import Power


class Player(Ship):
  score = 0
  score_increment = 10
  
  def __init__(self, x, y, width = 50, height = 50, health = 100, velocity = 5):
    super().__init__(x, y, width, height, health, velocity)
    self.ship_img = pygame.transform.scale(PLAYER_SPACE_SHIP, (width, height))
    self.laser_img = YELLOW_LASER
    self.mask = pygame.mask.from_surface(self.ship_img)
    self.max_health = health
  
  def draw(self, window):
    super().draw(window)
    self.move_power_ups()
    if self.health >= 0:
      self.health_bar(window)
      
  def increment_score(self):
    self.score += self.score_increment
    
  def spawn_power_up(self, x, y):
    if random.randrange(0, 3) == 1:
      power_up = Power(x, y, random.choice(["attack_speed", "add_laser", "movement_speed", "regenerate_health"]))
      self.power_ups.append(power_up)
      
  def move_power_ups(self):
    for power_up in self.power_ups:
      power_up.move()
      if power_up.off_screen(HEIGHT):
        self.power_ups.remove(power_up)
      else:
        if power_up.collision(self):
          if power_up.power_type == "attack_speed":
            self.reduce_cooldown()
          elif power_up.power_type == "add_laser":
            self.add_laser()
          elif power_up.power_type == "movement_speed":
            self.speed_up()
          elif power_up.power_type == "regenerate_health":
            self.health += 20
            if self.health > self.max_health:
              self.health = self.max_health
          self.power_ups.remove(power_up)
      
  def move_lasers(self, objs):
    self.cool_down()
    for laser in self.lasers:
      laser.move(-self.laser_velocity)
      if laser.off_screen(HEIGHT):
        self.lasers.remove(laser)
      else:
        # remove the laser and the object if it collides with an object
        for obj in objs:
          if laser.collision(obj):
            if obj.health > 0:
              obj.health -= 10
            if obj.health <= 0:
              objs.remove(obj)
              self.spawn_power_up(obj.x, obj.y)
              self.increment_score()
            if laser in self.lasers:
              self.lasers.remove(laser)
              
  def health_bar(self, window):
    pygame.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + (self.ship_img.get_height() // 7), self.ship_img.get_width(), 5), border_radius=10)
    pygame.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + (self.ship_img.get_height() // 7), self.ship_img.get_width() * (self.health / self.max_health), 5), border_radius=10)