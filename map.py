import pygame as pg
import random
from settings import *
_ = False
# mini_map = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, _, 1, 1, 1, 1, 1, _, _, 1, 1, 1, _, _, 1],
#     [1, _, _, _, _, _, _, 1, _, _, _, _, 1, _, _, 1],
#     [1, _, _, _, _, _, _, 1, _, _, _, _, 1, _, _, 1],
#     [1, _, _, _, _, _, _, 1, _, _, _, _, _, _, _, 1],
#     [1, _, _, 1, 1, 1, 1, 1, _, _, _, _, _, _, _, 1],
#     [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
#     [1, _, _, 1, _, _, _, _, 1, _, _, _, _, _, _, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     ]

class Map:
    def __init__(self, display, brain):
        self.display = display
        # self.mini_map = mini_map
        self.mini_map = brain.map
        # print(brain.map)
        self.world_map = {}
        self.get_map()
    
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i,j)] = value
    def draw(self):
        #[pg.draw.rect(self.display.screen, 'darkgray', (pos[0] * 10, pos[1] * 10, 10, 10), 2)
        #    for pos in self.world_map]
        for pos, value in self.world_map.items():
            if(value == -1):
                color = 'darkgray'
                pg.draw.rect(self.display.screen, color, (pos[0] * 10, pos[1] * 10, 10, 10))
            else:
                # Generate a random integer between 0 and 16777215 (0xFFFFFF in hexadecimal)
                random.seed(value)
                random_number = random.randint(0, 0xFFFFFF)
                # Convert the number to hexadecimal and format it as a color string
                color = "#{:06X}".format(random_number)
                pg.draw.circle(self.display.screen, color, (pos[0] * 10, pos[1] * 10), 10)
                # color = '#00FF00'