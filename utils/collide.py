def collide(obj1, obj2):
  offset_x = obj2.x - obj1.x
  offset_y = obj2.y - obj1.y
  # check if obj1 collided/overlapped with obj2 based on their pixel not by their w and h properties
  return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None