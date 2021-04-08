import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 480))
white = (255,255,255)
pygame.display.set_caption('Image')
screen.fill(white)
global running
running = True
while running:

    # Did the user click the window close button?

    abombImg = pygame.image.load('C:\Users\jerry\Pictures\abomb.png')
    gelatorImg = pygame.image.load('C:\Users\jerry\Pictures\gelator.png')
    kroakenImg = pygame.image.load('C:\Users\jerry\Pictures\kroaken.png')
    ericImg = pygame.image.load('C:\Users\jerry\Pictures\eric.png')
    nachosImg = pygame.image.load('C:\Users\jerry\Pictures\nachos.png')
    #carImg = pygame.image.load('racecar.png')
    #carImg = pygame.image.load('racecar.png')
    #carImg = pygame.image.load('racecar.png')

    screen.blit(abombImg, (0,0))
    screen.blit(gelatorImg, (350,200))
    screen.blit(kroakenImg, (550,200))
    screen.blit(ericImg, (700,200))
    screen.blit(nachosImg, (100,400))
    #gameDisplay.blit(carImg, (x,y))
    #gameDisplay.blit(carImg, (x,y))
    #gameDisplay.blit(carImg, (x,y))
    pygame.display.flip()

    for event in pygame.event.get() :
        if event.type == pygame.QUIT: 
            pygame.quit()
            quit()
    
#end main loop
