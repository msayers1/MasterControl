import pygame as pg
import sys
from settings import *
from robotBrain import RobotBrain
from map import *
from player import *
from raycasting import *

display_mode = '2d' # 2d
# display_mode = '3d' # 3d will not have the robots. 

class Display:
    def __init__(self, height, width, numberRobotMinions):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.delta_time = 1
        self.brain = RobotBrain(mapHeight, mapWidth, numberRobotMinions)
        #self.brain.print_Map()
        #self.brain.print_Robots()
        self.new_game()
        
        
    
    def new_game(self):
        if display_mode == '3d':
            self.map = Map(self, self.brain)
            self.player = Player(self)
            self.raycasting = RayCasting(self)
        else:
            self.map = Map(self, self.brain)
            

    def update(self):
        if display_mode == '3d':
            self.player.update()
            self.raycasting.update()
            pg.display.flip()
            self.delta_time = self.clock.tick(FPS)
            self.clock.tick(FPS)
            pg.display.set_caption(f'{self.clock.get_fps() : .1f}')
        else:
            self.brain.update()
            pg.display.flip()
            self.delta_time = self.clock.tick(FPS)
            self.clock.tick(FPS)
            pg.display.set_caption(f'{self.clock.get_fps() : .1f}')
    def draw(self):
        if display_mode == '3d':
            self.screen.fill('black')
        else:
            self.map.draw()
            # self.player.draw()

        
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                print(f"Quitting....")
                pg.quit()
                sys.exit()
                    
    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()
            
if __name__ == '__main__':
    display = Display()
    display.run()