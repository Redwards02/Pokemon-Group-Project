from random import randint
import pygame
import fight
import Rpi.GPIO as GPIO
switches = [18, 19, 20, 21]
GPIO.setmode(GPIO.BCM)
GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


#setup display
width, height = 800, 400
screen = pygame.display.set_mode((width, height))

# color
WHITE = (255, 255, 255)
RED = (255,0,0)
BLACK = (0,0,0)

# Images go here
#sprites
abombImg = pygame.image.load('abomb.png')
gelatorImg = pygame.image.load('gelator.png')
kroakenImg = pygame.image.load('kroaken.png')
ericImg = pygame.image.load('eric.png')
nachosImg = pygame.image.load('nachos.png')
brickdoopImg = pygame.image.load('brickdoop.png')
bottlerockerImg = pygame.image.load('bottlerocker.png')
dracolichImg = pygame.image.load('dracolich1.png')
arrowImg = pygame.image.load('arrow.png')

background = pygame.image.load("background.png")
#moves
attack1Img = pygame.image.load("attack1.png")
attack2Img = pygame.image.load("attack2.png")
attack3Img = pygame.image.load("attack3.png")
attack4Img = pygame.image.load("attack4.png")

FPS = 30


#all sprites go in thir spot in the menu
def displaySprites():
    screen.blit(abombImg, (40, 40))
    screen.blit(gelatorImg, (240, 30))
    screen.blit(kroakenImg, (420, 20))
    screen.blit(ericImg, (600, 20))
    screen.blit(nachosImg, (40, 180))
    screen.blit(brickdoopImg, (240, 220))
    screen.blit(bottlerockerImg, (420, 230))
    screen.blit(dracolichImg, (600, 180))


#moves around the arrow
def moveArrow(choiceIndex):
    if choiceIndex >= 8:
        choiceIndex = 7
    elif choiceIndex < 0:
        choiceIndex = 0
    if choiceIndex == 0:
        screen.blit(arrowImg, (100, 25))
    if choiceIndex == 1:
        screen.blit(arrowImg, (300, 25))
    if choiceIndex == 2:
        screen.blit(arrowImg, (500, 25))
    if choiceIndex == 3:
        screen.blit(arrowImg, (660, 25))
    if choiceIndex == 4:
        screen.blit(arrowImg, (100, 200))
    if choiceIndex == 5:
        screen.blit(arrowImg, (300, 200))
    if choiceIndex == 6:
        screen.blit(arrowImg, (500, 200))
    if choiceIndex == 7:
        screen.blit(arrowImg, (660, 200))
    return choiceIndex

#update the screen
def drawScreen():
    pygame.display.update()

#main loop for menu gui
def menuLoop():
    choiceIndex = 0
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        screen.fill(WHITE)
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 run = False
                 pygame.quit()
        # if GPIO.input(18) == 1:
        #     choiceIndex -= 1
        # elif gpio.input(19) == 1:
        #     choiceIndex += 1
        # elif GPIO.input(20) == 1:
        #     choiceIndex -= 4
        # elif gpio.input(21) == 1:
        #     choiceIndex += 4

            if event.type == pygame.KEYDOWN:
                if choiceIndex >= 8:
                    choiceIndex = 7
                elif choiceIndex < 0:
                    choiceIndex = 0
                if event.key == pygame.K_a:
                    run = False

                if event.key == pygame.K_b:
                    pass
                if event.key == pygame.K_LEFT and choiceIndex != 0:
                    choiceIndex -= 1
                if event.key == pygame.K_RIGHT and choiceIndex != 7:
                    choiceIndex += 1
                if event.key == pygame.K_DOWN and choiceIndex != (4 or 5 or 6 or 7):
                    choiceIndex += 4
                if event.key == pygame.K_UP and choiceIndex != (0 or 1 or 2 or 3):
                    choiceIndex -= 4


        displaySprites()
        moveArrow(choiceIndex)
        drawScreen()
    return choiceIndex

#selects image for the player
def playerSprite(choiceIndex):
    if choiceIndex == 0:
        return pygame.image.load('abomb.png')
    if choiceIndex == 1:
        return pygame.image.load('gelator.png')
    if choiceIndex == 2:
        return pygame.image.load('kroaken.png')
    if choiceIndex == 3:
        return pygame.image.load('eric.png')
    if choiceIndex == 4:
        return pygame.image.load('nachos.png')
    if choiceIndex == 5:
        return pygame.image.load('brickdoop.png')
    if choiceIndex == 6:
        return pygame.image.load('bottlerocker.png')
    if choiceIndex == 7:
        return pygame.image.load('dracolich1.png')

#displays the player
def displayPlayer(playerImage):
    screen.blit(playerImage, (50, 200))

#displays the enemy
def displayEnenmy(enemyIndex):
    enemyImage = playerSprite(enemyIndex)
    screen.blit(enemyImage, (550, 25))

#displays and updates health bars
def displayHealth(p1,p2):
    pygame.draw.rect(screen, RED, (300, 250, p1.health, 5))
    pygame.draw.rect(screen, RED, (400, 100, p2.health, 5))

#show names as text
def displaySpriteNames():
    pass

#show selection of moves
def displayMoves():
    screen.blit(attack1Img, (500, 300))
    screen.blit(attack2Img, (650, 300))
    screen.blit(attack3Img, (500, 350))
    screen.blit(attack4Img, (650, 350))

#detects if a player has died
def determineDeath(p1, p2):

    if p1.health<=0:
        pygame.time.delay(1000)
        return p2, False

    elif p2.health<=0:
        pygame.time.delay(1000)
        return p1, False


    else:
        pass

#turns the players into objects with respective stats
def initializePlayer(choiceIndex):
    if choiceIndex == 0:
        return fight.Nabomb()
    elif choiceIndex == 1:
        return fight.Gelator()
    elif choiceIndex == 2:
        return fight.Kroaken()
    elif choiceIndex == 3:
        return fight.Eric()
    elif choiceIndex == 4:
        return fight.Nachos()
    elif choiceIndex == 5:
        return fight.Brickdoop()
    elif choiceIndex == 6:
        return fight.Bottlerocker()
    elif choiceIndex == 7:
        return fight.Dracolich()

#moves the arrow around moves
def displayArrow(attackIndex):
    if attackIndex == 0:
        screen.blit(arrowImg, (500, 300))
    if attackIndex == 1:
        screen.blit(arrowImg, (650, 300))
    if attackIndex == 2:
        screen.blit(arrowImg, (500, 350))
    if attackIndex == 3:
        screen.blit(arrowImg, (650, 350))
    return attackIndex
def displayText(pokemon, other, attackIndex, time, enemyAttackIndex):
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 18)
    print(time)
    enemysTurn = False
    if time < 90:
        textsurface = myfont.render(pokemon.getText(attackIndex), False, (0, 0, 0))
        screen.blit(textsurface, (0, 0))
        enemysTurn = True
    if (time>90) :
        textsurface = myfont.render(" ", False, (0, 0, 0))

        screen.blit(textsurface, (0, 0))
        if time == 99:
            other.attack(pokemon)
        enemysTurn = False
        if time < 180:
            textsurface = myfont.render(other.getText(enemyAttackIndex), False, (0, 0, 0))
        screen.blit(textsurface, (0, 0))



#main loop for game gui
def gameLoop(choiceIndex):
    enemyIndex = randint(0, 7)
    clock = pygame.time.Clock()
    playerImage = playerSprite(choiceIndex)
    run = True
    screen.fill(WHITE)
    p1 = initializePlayer(choiceIndex)
    p2 = initializePlayer(enemyIndex)
    attackIndex = 0
    time = 10000
    enemyAttackIndex = 0
    while run:
        clock.tick(FPS)
        #screen.fill(WHITE)
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if time>180:
                    if event.key == pygame.K_LEFT:
                        attackIndex -= 1
                    if event.key == pygame.K_RIGHT:
                        attackIndex += 1
                    if event.key == pygame.K_DOWN:
                        attackIndex += 2
                    if event.key == pygame.K_UP:
                        attackIndex -= 2
                    if event.key == pygame.K_a:
                        p1.attack(p2)
                        time = 0
                        enemyAttackIndex = randint(0,3)



        print("hi")
        displayText(p1, p2, attackIndex, time, enemyAttackIndex)
        displayArrow(attackIndex)
        displayEnenmy(enemyIndex)
        displayPlayer(playerImage)
        displayHealth(p1,p2)
        #displaySpriteNames()
        displayMoves()
        drawScreen()
        winner = determineDeath(p1,p2)
        if (p1.health <= 0):
            winner = p2
            return winner
            run = False
        if (p2.health <= 0):
            winner = p1
            return winner
            run = False

        time += 1

def victoryLoop(winner):
    run = True
    clock = pygame.time.Clock()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        clock.tick(FPS)
        screen.fill(WHITE)
        pygame.font.init()
        myfont = pygame.font.SysFont('Comic Sans MS', 18)
        textsurface = myfont.render("{} has won the battle".format(winner.name), False, (0, 0, 0))
        screen.blit(textsurface, (0, 0))
        screen.blit(winner.img, (300,100))


        drawScreen()

# Main Code
choiceIndex = menuLoop()
winner = gameLoop(choiceIndex)
victoryLoop(winner)
