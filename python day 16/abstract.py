from abc import ABC, abstractmethod
import math

class shape(ABC):
    @abstractmethod
    def area(self):
     pass
class circle(shape):
   def __init__(self,radius):
    self.radius = radius
   def area(self):
     return math.pi*self.radius**2
class rectangle(shape):
    def __init__(self,length,width):
     self.length = length
     self.width = width
    def area(self):
     return self.length*self.width 
c = circle(5)
r = rectangle(7,8)
print (c.area())
print(r.area())