import numpy as np
import math
speedX = 10
speedY = 10

class RobotMinion:
    def __init__(self, name, sX, sY):
        self.location = self.x, self.y = sX, sY
        self.name = name

    def __init__(self, name, location):
        self.location = self.x, self.y = location[0], location[1]
        self.name = name
    def move(self, dX, dY):
        self.x += dX
        self.y += dY

    def destination(self, inputMethod, aX, aY):
        if inputMethod == 'point':
            distanceX = aX - self.x
            distanceY = aY - self.y
            dX = distanceX // speedX
            dY = distanceY // speedY
            print(f"Before {self.location}")
            self.move(dX, dY)
            #self.destination('point', aX, aY)
            print(f"After {self.location}")
        elif inputMethod == 'direction':    
            distanceX = aX - self.x
            distanceY = aY - self.y
            dX = distanceX // speedX
            dY = distanceY // speedY
            self.move(dX, dY)
            #self.destination('point', aX, aY)
    
    def print_location(self):
        print(self.location)