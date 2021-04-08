#CSC 132 Final Project
#Reese Edwards, Cayden Reed, Luke Harper
import pygame
from pygame.locals import *
class Pokemon:
    def __init__(self, typing, health):
        self.typing = typing
        self.moves = moves
    #moves all pokemon have
        
    def headbutt(self):
        pass
        
    def pound(self):
        pass
        
    #types and type specific moves

class Fire(Pokemon):
    def flamethrower():
        pass

    def ignite():
        pass

class Water(Pokemon):
    def tidalWave():
        pass

    def hydroPump(Pokemon):
        pass

class Grass(Pokemon):
    def bulletSeed():
        pass
        
    def razorLeaf():
        pass

class Ghost(Pokemon):
    def lick():
        pass

    def haunt():
        pass
class Psychic(Pokemon):
    def confuson():
        pass

    def extrasensory():
        pass

class Rock(Pokemon):
    def rockTomb():
        pass

    def rockThrow():
        pass
    

class Flying(Pokemon):
    def wingAttack():
        pass

    def fly():
        pass

class Dragon(Pokemon):
    def dragonDance():
        pass

    def dragonBreath():
        pass


class Nabomb(Fire):
    def __init__(self, attack, defense, spAttack, spDefense, health, speed):
        self.attack = attack
        self.health = health
        self.defense = defense
        self.speed = speed
        
class Gelator(Water):
    def __init__(self, attack, defense, spAttack, spDefense, health, speed):
        self.attack = attack
        self.health = health
        self.defense = defense
        self.speed = speed

class Kroaken(Grass):
    def __init__(self, attack, defense, spAttack, spDefense, health, speed):
        self.attack = attack
        self.health = health
        self.defense = defense
        self.speed = speed

class Eric(Ghost):
    def __init__(self, attack, defense, spAttack, spDefense, health, speed):
        self.attack = attack
        self.health = health
        self.defense = defense
        self.speed = speed

class Nachos(Psychic):
    def __init__(self, attack, defense, spAttack, spDefense, health, speed):
        self.attack = attack
        self.health = health
        self.defense = defense
        self.speed = speed

class Brickdoop(Rock):
    def __init__(self, attack, defense,spAttack, spDefense, health, speed):
        self.attack = attack
        self.health = health
        self.defense = defense
        self.speed = speed

class Bottlerocker():
    def __init__(self, attack, defense, spAttack, spDefense, health, speed):
        self.attack = attack
        self.health = health
        self.defense = defense
        self.speed = speed

class Dracolich(Pokemon):
    def __init__(self, attack, defense, spAttack, spDefense, health, speed):
        self.attack = attack
        self.health = health
        self.defense = defense
        self.speed = speed

#******************************* GUI ***************************************


def pickNabomb(x,y):
    gameDisplay.blit(nabombSprite, (x,y))
def pickGelator(x,y):
    gameDisplay.blit(nabombSprite, (x,y))
def pickNabomb(x,y):
    gameDisplay.blit(nabombSprite, (x,y))
def pickNabomb(x,y):
    gameDisplay.blit(nabombSprite, (x,y))
def pickNabomb(x,y):
    gameDisplay.blit(nabombSprite, (x,y))
def pickNabomb(x,y):
    gameDisplay.blit(nabombSprite, (x,y))
def pickNabomb(x,y):
    gameDisplay.blit(nabombSprite, (x,y))
def pickNabomb(x,y):
    gameDisplay.blit(nabombSprite, (x,y))

        
#Health Bars


def get_pygame_events():
  pygame_events = pygame.event.get()
  return pygame_events
def menu():
    nabomb = Nabomb(97, 54, 75, 75, 52, 7)
    gelator = Gelator(45, 84, 95, 75, 75 ,1)
    kroaken = Kroaken(56, 75, 87, 75, 75, 3)
    eric = Eric(56, 75, 87, 75, 75, 3)
    nachos = Nachos(56, 75, 87, 75, 75, 3)
    brickdoop = Brickdoop(56, 75, 87, 75, 75, 3)
    bottlerocker = Bottlerocker(56, 75, 87, 75, 75, 3)
    dracolich = Dracolich(56, 75, 87, 75, 75, 3)
    
    abombImg = pygame.image.load('abomb.png')
    gelatorImg = pygame.image.load('gelator.png')
    kroakenImg = pygame.image.load('kroaken.png')
    ericImg = pygame.image.load('eric.png')
    nachosImg = pygame.image.load('nachos.png')
    #carImg = pygame.image.load('racecar.png')
    #carImg = pygame.image.load('racecar.png')
    #carImg = pygame.image.load('racecar.png')

    screen.blit(abombImg, (40,75))
    screen.blit(gelatorImg, (240,75))
    screen.blit(kroakenImg, (400,30))
    screen.blit(ericImg, (600,75))
    screen.blit(nachosImg, (40,200))
    #gameDisplay.blit(carImg, (x,y))
    #gameDisplay.blit(carImg, (x,y))
    #gameDisplay.blit(carImg, (x,y))
    pygame.display.flip()



    #list of pokemon

    choices = {nabomb:1,gelator:2,kroaken:3,eric:4,nachos:5,brickdoop:6,bottlerocker:7,dracolich:8}
    
    choiceIndex = 1
    finalChoice = pick(choiceIndex)
    print(finalChoice)
    #return the pokemon chosen as its class
    return choices[finalChoice]


def highlightCurrent(choiceIndex):
    arrowImg = pygame.image.load('arrow.png')
    if choiceIndex == 1:
        screen.blit(arrowImg, (40,25))
        pygame.display.flip()
    elif choiceIndex == 2:
        screen.blit(arrowImg, (240,25))
        pygame.display.flip()
    elif choiceIndex == 3:
        screen.blit(arrowImg, (400,25))
        pygame.display.flip()
    elif choiceIndex == 4:
        screen.blit(arrowImg, (600,25))
        pygame.display.flip()
    elif choiceIndex == 5:
        screen.blit(arrowImg, (10,75))
        pygame.display.flip()
    elif choiceIndex == 6:
        screen.blit(arrowImg, (10,75))
        pygame.display.flip()
    elif choiceIndex == 7:
        screen.blit(arrowImg, (10,75))
        pygame.display.flip()
    elif choiceIndex == 8:
        screen.blit(arrowImg, (10,75))
        pygame.display.flip()

def pick(choiceIndex):
    keys_pressed = get_pygame_events()
    picking = True
    highlightCurrent(choiceIndex)
    while picking == True:
        for event in keys_pressed:
            if event.type == pygame.KEYDOWN:
                if((event.key == K_LEFT) and (choiceIndex != 1 or 5)):
                    choiceIndex -=1
                    highlightCurrent(choiceIndex)
                elif ((event.key == K_RIGHT) and (choiceIndex != 4 or 8)):
                    choiceIndex +=1
                    highlightCurrent(choiceIndex)
                elif ((event.key == K_UP) and (choiceIndex != 1 or 2 or 3 or 4)):
                    choiceIndex -=4
                    highlightCurrent(choiceIndex)
                elif ((event.key == K_DOWN) and (choiceIndex != 5 or 6 or 7 or 8)):
                    choiceIndex +=4
                    highlightCurrent(choiceIndex)
                if event.key == K_a:
                    return choiceIndex
                    picking = False
                else:
                    pass
            elif event.type == pygame.QUIT:
                pygame.quit()


        
                
def battle():
    pass




#********************** main code *******************
pygame.init()
screen = pygame.display.set_mode((800, 480))
white = (255,255,255)
pygame.display.set_caption('Caydenmon')
screen.fill(white)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    menu()
    running = False
#end main loop

pygame.quit()



