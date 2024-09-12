

# def main():
import threading
import time
# from robotBrain import RobotBrain
from display import Display
import random 
from settings import *

numberOfRobots = 20

def print_cube(num):
    time.sleep(100)
    print("Cube: {}" .format(num * num * num))


def print_square(num):
    time.sleep(10)
    print("Square: {}" .format(num * num))


if __name__ =="__main__":
    # brain = RobotBrain(20, 20, 4)
    # brain.print_Map()
    # brain.print_Robots()
    display = Display(HEIGHT, WIDTH, numberOfRobots)
    display.run()


    # t1 = threading.Thread(target=print_square, args=(10,))
    # t2 = threading.Thread(target=print_cube, args=(10,))

    # t2.start()
    # t1.start()

    # t1.join()
    # t2.join()

    # print("Done!")

# if __name__ == "__main__":
#     main()
