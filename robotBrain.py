import numpy as np
from robotModules import RobotMinion
import random 

class RobotBrain:
    def __init__(self, height, width, numberRobotMinions):
        self.create_map(height, width)
        self.mapSize = self.mapHeight, self.mapWidth = height, width
        # print(height)
        # print(width)
        # print(self.map.shape)
        self.RobotMinions = []
        startingLocations = set()
        for i in range(numberRobotMinions):
            while True:
                # Generate two random numbers, one from 1 to var1_max and another from 1 to var2_max
                ranX = random.randint(1, width-2)
                ranY = random.randint(1, height-2)
                pair = (ranY, ranX)
  
                # Ensure that the pair is unique
                if pair not in startingLocations:
                    startingLocations.add(pair)
                    # print(pair)
                    newRobotMinion = RobotMinion(f"robot{i+1}", pair)
                    self.RobotMinions.append(newRobotMinion)
                    self.map[ranY][ranX] = i+1
                    break
        
    def create_map(self, height, width):
        # Create a 2D NumPy array initialized with zeros
        dynamic_map = np.zeros((height, width), dtype=int)
        # Assign 1 to the first and last row
        dynamic_map[0, :] = -1
        dynamic_map[-1, :] = -1

        # Assign 1 to the first and last column
        dynamic_map[:, 0] = -1
        dynamic_map[:, -1] = -1
        self.map = dynamic_map

    def update(self):
        for robot in self.RobotMinions:
            # Generate two random numbers, one from 1 to var1_max and another from 1 to var2_max
            ranX = random.randint(1, self.mapWidth-2)
            ranY = random.randint(1, self.mapHeight-2)
            pair = (ranY, ranX)
            robot.destination('point', ranX, ranY)
    def print_Robots(self):
        for robot in self.RobotMinions:
            print(f"{robot.name} is at {robot.x} by {robot.y} or ({robot.location})")

    def print_Map(self):
        print(self.map)