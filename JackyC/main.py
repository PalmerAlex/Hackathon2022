import pygame
import os
import random

WIDTH, HEIGHT = 1280, 720 #width and height of game window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("testing")
WHITE = (255, 255, 255)
numPlayers = random.randint(1, 4)
numObst = numPlayers * 4
FPS = 60
WALL_IMG = pygame.image.load(os.path.join('Hackathon2022\JackyC\JackyAssets','wall.png'))

class Entity():  
    def __init__(self) -> None:
        pass
    # checklist
    # - What shared/abstract methods do we want for this class

class obstacle(Entity): #class for obstacle
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
        self.WALL = pygame.transform.scale(WALL_IMG, (width, height))
    # checklist
    # implement object collisions 
    # spread out the boxes a bit more +-25

def draw_window():
    WIN.fill(WHITE)
    pygame.display.update()

def take_arr():
    xArr = []
    yArr = []
    for i in range(0, numObst):
        x = 1*random.randint(100, 1180)
        y = 1*random.randint(100, 620)
        xArr.append(x)
        yArr.append(y)
    return (xArr, yArr)

def draw_boxes(xArr, yArr):
    obst = obstacle(50, 50)
    for i in range(0, numObst):
        WIN.blit(obst.WALL, (xArr[i], yArr[i]))
    pygame.display.update()

def collide_action(xArr, yArr):
    obst = obstacle(50, 50)
    for i in range(0, numObst):
        WALL_Rect = obst.WALL.get_rect(center=(xArr[i], yArr[i]))
        if(WALL_Rect.colliderect()): #implement collisions  
            pass

def gameInstance():
    clock = pygame.time.Clock()
    inst = True
    twoTuple = take_arr()
    draw_window()
    draw_boxes(twoTuple[0], twoTuple[1])
    while inst:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inst = False
        
    pygame.quit()

if __name__ == "__main__":
    gameInstance()
