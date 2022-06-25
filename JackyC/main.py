import pygame
import os
import random

WIDTH, HEIGHT = 1280, 720 #width and height of game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("testing")
WHITE = (255, 255, 255)
numPlayers = random.randint(1, 4)
FPS = 60
WALL_IMG = pygame.image.load(os.path.join('Hackathon2022\Assets', 'wall.png'))

# class Menu(object):
#     def __init__(self, title) -> None: #class for menu 
#         self.title = title
#     def testFunc (self)-> str:
#         return self.title

# class gameInstance(Menu): #class for gameInstance
#     def __init__(self) -> None:
#         pass
# class Arena(gameInstance): #class for Arena 
#     def __init__(self) -> None:
#         pass

class Entity(): #class for Entity, remeber that it extends Arena 
    def __init__(self) -> None:
        pass
    # checklist
    # - What shared/abstract methods do we want for this class

class Tank(Entity): #class for Tank
    def __init__(self, dmg) -> None:
        self.dmg = dmg

class obstacle(Entity): #class for obstacle
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.WALL = pygame.transform.scale(WALL_IMG, (width, height))

    # checklist
    # - set pos of each obstacle and have more when each player joins 
    # - do we want the objects to break?
        
# class Powerup(Entity): #class for Powerup
#     def __init__(self) -> None:
#         self.powerupWidth = 10
#         self.powerupHeight = 10
#     # checklist
#     # - what kinds of powerups do we want on the map?
# class health(Powerup):
#     def __init__(self) -> None:
#         super().__init__()
# #integers for random block generation

def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()

def take_arr():
    xArr = []
    yArr = []
    for i in range(0, 10*numPlayers):
        x = 1*random.randint(100, 1180)
        y = 1*random.randint(100, 620)
        xArr.append(x)
        yArr.append(y)
    return (xArr, yArr)

def draw_boxes(xArr, yArr):
    obst = obstacle(50, 50)
    for i in range(0, 10*numPlayers):
        WIN.blit(obst.WALL, (xArr[i], yArr[i]))
    pygame.display.update()

def gameInstance():
    clock = pygame.time.Clock()
    inst = True
    twoTuple = take_arr()
    while inst:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inst = False
        draw_window()
        draw_boxes(twoTuple[0], twoTuple[1])

    pygame.quit()

if __name__ == "__main__":
    gameInstance()
