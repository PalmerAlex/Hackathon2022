import pygame

class Menu(object):
    def __init__(self, title) -> None: #class for menu 
        self.title = title
    def testFunc (self)-> str:
        return self.title

class gameInstance(Menu): #class for gameInstance
    def __init__(self) -> None:
        pass
class Arena(gameInstance): #class for Arena 
    def __init__(self) -> None:
        pass

class Entity(Arena): #class for Entity
    def __init__(self) -> None:
        pass

class Tank(Entity): #class for Tank
    def __init__(self, dmg) -> None:
        self.dmg = dmg


class obstacle(Entity): #class for obstacle
    def __init__(self, width, height) -> None:
        self.height = height
        self.width = width
        
class Powerup(Entity): #class for Powerup
    def __init__(self, powerupName) -> None:
        self.powerupName = powerupName
