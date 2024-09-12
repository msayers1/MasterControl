import pygame as pg
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
        [pg.draw.rect(self.display.screen, 'darkgray', (pos[0] * 10, pos[1] * 10, 10, 10), 2)
            for pos in self.world_map]