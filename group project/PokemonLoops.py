from random import randint
import pygame
import fight
# import Rpi.GPIO as GPIO
from time import sleep

#
# switches = [18, 19, 20, 21, 22]
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(switches, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

# setup display
width, height = 800, 480
screen = pygame.display.set_mode((width, height))

# color
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
PURPLE = (240, 0, 255)

pokemonList = [fight.Nabomb(), fight.Gelator(), fight.Kroaken(), fight.Eric(), fight.Nachos(), fight.Brickdoop(),
               fight.Bottlerocker(), fight.Dracolich()]
enemyPokemonList = [fight.Nabomb(), fight.Gelator(), fight.Kroaken(), fight.Eric(), fight.Nachos(), fight.Brickdoop(),
               fight.Bottlerocker(), fight.Dracolich()]
# Images go here
# sprites
abombImg = pygame.image.load('abomb.png')
gelatorImg = pygame.image.load('gelator.png')
kroakenImg = pygame.image.load('kroaken.png')
ericImg = pygame.image.load('eric.png')
nachosImg = pygame.image.load('nachos.png')
brickdoopImg = pygame.image.load('brickdoop.png')
bottlerockerImg = pygame.image.load('bottlerocker.png')
dracolichImg = pygame.image.load('dracolich.png')
arrowImg = pygame.image.load('arrow.png')

boxImg = pygame.image.load("box.png")
openBoxImg = pygame.image.load("boxOpen.png")
boxLidImg = pygame.image.load("boxLid.png")

abombRect = (width / 8, height / 6, 165, 117)

background = pygame.image.load("background.png")
menuBackground = pygame.image.load("menu.png")

chartImg = pygame.image.load("chart.png")
# moves
attack1Img = pygame.image.load("attack1.png")
attack2Img = pygame.image.load("attack2.png")
attack3Img = pygame.image.load("attack3.png")
attack4Img = pygame.image.load("attack4.png")

# animation images
rockImg = pygame.image.load("rock.png")

FPS = 30


def displayStats(choiceIndex):
    if choiceIndex >= 8:
        choiceIndex = 7
    elif choiceIndex < 0:
        choiceIndex = 0
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 18)
    attackTextSurface = myfont.render("Atk: {}".format(pokemonList[choiceIndex].atk), False, BLACK)
    screen.blit(attackTextSurface, (575, 50))
    defenseTextSurface = myfont.render("Def: {}".format(pokemonList[choiceIndex].defense), False, BLACK)
    screen.blit(defenseTextSurface, (575, 70))
    healthTextSurface = myfont.render("Health: {}".format(pokemonList[choiceIndex].health), False, BLACK)
    screen.blit(healthTextSurface, (575, 90))
    typeTextSurface = myfont.render("Type: {}".format(pokemonList[choiceIndex].types), False, BLACK)
    screen.blit(typeTextSurface, (575, 110))
    typeTextSurface = myfont.render(pokemonList[choiceIndex].getDescription(), False, BLACK)
    screen.blit(typeTextSurface, (410, 250))


def displaySprite(choiceIndex):
    if choiceIndex >= 8:
        choiceIndex = 7
    elif choiceIndex < 0:
        choiceIndex = 0

    screen.blit(pokemonList[choiceIndex].img, (400, 50))


# all sprites go in thir spot in the menu
def displaySprites(choiceIndex, time, lidRect):
    if choiceIndex >= 8:
        choiceIndex = 7
    elif choiceIndex < 0:
        choiceIndex = 0
    if choiceIndex != 0:
        screen.blit(boxImg, (100, 75))
    if choiceIndex != 1:
        screen.blit(boxImg, (200, 75))
    if choiceIndex != 2:
        screen.blit(boxImg, (100, 175))
    if choiceIndex != 3:
        screen.blit(boxImg, (200, 175))
    if choiceIndex != 4:
        screen.blit(boxImg, (100, 275))
    if choiceIndex != 5:
        screen.blit(boxImg, (200, 275))
    if choiceIndex != 6:
        screen.blit(boxImg, (100, 375))
    if choiceIndex != 7:
        screen.blit(boxImg, (200, 375))

    if choiceIndex == 0:
        screen.blit(openBoxImg, (100, 75))
        lidRect = animateLid(choiceIndex, time, lidRect)
    if choiceIndex == 1:
        screen.blit(openBoxImg, (200, 75))
        lidRect = animateLid(choiceIndex, time, lidRect)
    if choiceIndex == 2:
        screen.blit(openBoxImg, (100, 175))
        lidRect = animateLid(choiceIndex, time, lidRect)
    if choiceIndex == 3:
        screen.blit(openBoxImg, (200, 175))
        lidRect = animateLid(choiceIndex, time, lidRect)
    if choiceIndex == 4:
        screen.blit(openBoxImg, (100, 275))
        lidRect = animateLid(choiceIndex, time, lidRect)
    if choiceIndex == 5:
        screen.blit(openBoxImg, (200, 275))
        lidRect = animateLid(choiceIndex, time, lidRect)
    if choiceIndex == 6:
        screen.blit(openBoxImg, (100, 375))
        lidRect = animateLid(choiceIndex, time, lidRect)
    if choiceIndex == 7:
        screen.blit(openBoxImg, (200, 375))
        lidRect = animateLid(choiceIndex, time, lidRect)
    return lidRect


# moves around the arrow
def animateLid(choiceIndex, time, lidRect):
    if time == 0:
        if choiceIndex == 0:
            lidRect = pygame.Rect(100, 75, 54, 24)
        if choiceIndex == 1:
            lidRect = pygame.Rect(200, 75, 54, 24)
        if choiceIndex == 2:
            lidRect = pygame.Rect(100, 175, 54, 24)
        if choiceIndex == 3:
            lidRect = pygame.Rect(200, 175, 54, 24)
        if choiceIndex == 4:
            lidRect = pygame.Rect(100, 275, 54, 24)
        if choiceIndex == 5:
            lidRect = pygame.Rect(200, 275, 54, 24)
        if choiceIndex == 6:
            lidRect = pygame.Rect(100, 375, 54, 24)
        if choiceIndex == 7:
            lidRect = pygame.Rect(200, 375, 54, 24)
    if time < 30:
        lidRect.y -= 1
    return lidRect


# update the screen
def drawScreen():
    pygame.display.update()

def displayPicks(choiceIndexList):
    spot = 0
    x, y = 400, 375
    for i in range(len(choiceIndexList)):
        img = pokemonList[choiceIndexList[spot]].img
        smallImage = pygame.transform.scale(img, ())
        screen.blit(smallImage, (x,y))
        spot+=1
        x+=100


# def detectInput(event.key):
# if event.type == pygame.KEYDOWN:
#     if time > 180:
#         if event.key == pygame.K_LEFT:
#             attackIndex -= 1
#         if event.key == pygame.K_RIGHT:
#             attackIndex += 1
#         if event.key == pygame.K_DOWN:
#             attackIndex += 2
#         if event.key == pygame.K_UP:
#             attackIndex -= 2
#         if event.key == pygame.K_a:
#             p1.attack(p2)
#             animation.x = 50
#             animation.y = 300
#             enemyAnimation.x = 550
#             enemyAnimation.y = 25
#             time = 0
#             enemyAttackIndex = randint(0, 3)
# main loop for menu gui
def menuLoop():
    # global event
    choiceIndex = 0
    clock = pygame.time.Clock()
    run = True
    lidRect = pygame.Rect(100, 75, 54, 24)
    time = 1000
    choiceIndexList = []
    while run:
        clock.tick(FPS)
        # screen.fill(WHITE)
        screen.blit(menuBackground, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if choiceIndex >= 8:
                    choiceIndex = 7
                elif choiceIndex < 0:
                    choiceIndex = 0
                if event.key == pygame.K_a:
                    choiceIndexList.append(choiceIndex)
                    if len(choiceIndexList) == 3:
                        print(choiceIndexList)
                        run = False
                if event.key == pygame.K_b:
                    pass
                if event.key == pygame.K_LEFT:
                    choiceIndex -= 1
                    time = 0
                if event.key == pygame.K_RIGHT:
                    choiceIndex += 1
                    time = 0
                if event.key == pygame.K_DOWN:
                    choiceIndex += 2
                    time = 0
                if event.key == pygame.K_UP:
                    choiceIndex -= 2
                    time = 0
        # if GPIO.input(18) == 1:
        #     choiceIndex -= 1
        #     sleep(.3)
        # elif gpio.input(19) == 1:
        #     choiceIndex += 1
        #     sleep(.3)
        # elif GPIO.input(20) == 1:
        #     choiceIndex -= 4
        #     sleep(.3)
        # elif gpio.input(21) == 1:
        #     choiceIndex += 4
        #     sleep(.3)
        # elif gpio.imput(22) == 1:
        #     run = False
        displaySprite(choiceIndex)
        lidRect = displaySprites(choiceIndex, time, lidRect)
        screen.blit(boxLidImg, lidRect)
        # moveArrow(choiceIndex)
        screen.blit(chartImg, (400, 50))
        displayPicks(choiceIndexList)
        displayStats(choiceIndex)
        drawScreen()
        time += 1
    sleep(.3)
    return choiceIndexList


# selects image for the player
def playerSprite(choiceIndex):
    return pokemonList[choiceIndex].img


# displays the player
def displayPlayer(playerImage):
    screen.blit(playerImage, (50, 320))


# displays the enemy
def displayEnenmy(enemyPokemonOut):
    enemyImage = enemyPokemonOut.img
    screen.blit(enemyImage, (550, 25))


# displays and updates health bars
def displayHealth(p1, p2):
    pygame.draw.rect(screen, RED, (300, 250, p1.health, 5))
    pygame.draw.rect(screen, RED, (400, 100, p2.health, 5))


# show names as text
def displaySpriteNames():
    pass


# show selection of moves
def displayMoves(p1, p2, attackIndex):
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 18)
    if attackIndex == 0:
        attack1TextSurface = myfont.render(p1.moveNames[0], False, PURPLE)
        screen.blit(attack1TextSurface, (450, 350))
    else:
        attack1TextSurface = myfont.render(p1.moveNames[0], False, BLACK)
        screen.blit(attack1TextSurface, (450, 350))
    if attackIndex == 1:
        attack2TextSurface = myfont.render(p1.moveNames[1], False, PURPLE)
        screen.blit(attack2TextSurface, (600, 350))
    else:
        attack2TextSurface = myfont.render(p1.moveNames[1], False, BLACK)
        screen.blit(attack2TextSurface, (600, 350))
    if attackIndex == 2:
        attack3TextSurface = myfont.render(p1.moveNames[2], False, PURPLE)
        screen.blit(attack3TextSurface, (450, 400))
    else:
        attack3TextSurface = myfont.render(p1.moveNames[2], False, BLACK)
        screen.blit(attack3TextSurface, (450, 400))
    if attackIndex == 3:
        attack4TextSurface = myfont.render(p1.moveNames[3], False, PURPLE)
        screen.blit(attack4TextSurface, (600, 400))
    else:
        attack4TextSurface = myfont.render(p1.moveNames[3], False, BLACK)
        screen.blit(attack4TextSurface, (600, 400))


# detects if a player has died
def determineDeath(playerPokemonOut, enemyPokemonOut):
    if playerPokemonOut.health <= 0:
        pass

    if enemyPokemonOut.health <= 0:
        pass

    else:
        pass


# turns the players into objects with respective stats
def initializePlayer(choiceIndex):
    # if choiceIndex == 0:
    #     return fight.Nabomb()
    # elif choiceIndex == 1:
    #     return fight.Gelator()
    # elif choiceIndex == 2:
    #     return fight.Kroaken()
    # elif choiceIndex == 3:
    #     return fight.Eric()
    # elif choiceIndex == 4:
    #     return fight.Nachos()
    # elif choiceIndex == 5:
    #     return fight.Brickdoop()
    # elif choiceIndex == 6:
    #     return fight.Bottlerocker()
    # elif choiceIndex == 7:
    #     return fight.Dracolich()
    print(choiceIndex)
    print("^")
    return pokemonList[choiceIndex]
def initializeEnemy(choiceIndex):
    return enemyPokemonList[choiceIndex]

def displayText(pokemon, other, attackIndex, time, enemyAttackIndex):
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 18)
    enemysTurn = False
    if time < 90:
        textsurface = myfont.render(pokemon.getText(attackIndex), False, (0, 0, 0))
        screen.blit(textsurface, (30, 27))
        enemysTurn = True
    if (time > 90):
        textsurface = myfont.render(" ", False, (0, 0, 0))

        screen.blit(textsurface, (30, 27))
        if time == 99:
            other.attack(pokemon)
        enemysTurn = False
        if time < 180:
            textsurface = myfont.render(other.getText(enemyAttackIndex), False, (0, 0, 0))
        screen.blit(textsurface, (30, 27))


def displayAnimation(animation, pokemon, attackIndex):
    animationImg = pygame.image.load("{}".format(pokemon.moveImgs[attackIndex]))
    screen.blit(animationImg, animation)
    if animation.x <= 600:
        animation.x += 15
        animation.y -= 6
    else:
        pass

    return animation


def displayEnemyAnimation(enemyAnimation, pokemon, enemyAttackIndex):
    animationImg = pygame.image.load("{}".format(pokemon.moveImgs[enemyAttackIndex]))
    screen.blit(animationImg, enemyAnimation)
    if enemyAnimation.x >= 50:
        enemyAnimation.x -= 15
        enemyAnimation.y += 6
    else:
        pass

    return enemyAnimation


# main loop for game gui
def gameLoop(choiceIndexList):
    enemyIndexList = []
    for i in range(3):
        enemyIndexList.append(randint(0, 7))
    clock = pygame.time.Clock()
    run = True
    screen.fill(WHITE)
    p1p1 = initializePlayer(choiceIndexList[0])
    p1p2 = initializePlayer(choiceIndexList[1])
    p1p3 = initializePlayer(choiceIndexList[2])
    p2p1 = initializeEnemy(enemyIndexList[0])
    p2p2 = initializeEnemy(enemyIndexList[1])
    p2p3 = initializeEnemy(enemyIndexList[2])

    attackIndex = 0
    time = 10000
    enemyAttackIndex = 0
    animation = pygame.Rect(50, 300, 30, 50)
    enemyAnimation = pygame.Rect(550, 25, 30, 50)
    playerPokemonOut = p1p1
    enemyPokemonOut = p2p1
    move = False
    while run:

        clock.tick(FPS)
        # screen.fill(WHITE)
        screen.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if time > 180:
                    if event.key == pygame.K_LEFT:
                        attackIndex -= 1
                    if event.key == pygame.K_RIGHT:
                        attackIndex += 1
                    if event.key == pygame.K_DOWN:
                        attackIndex += 2
                    if event.key == pygame.K_UP:
                        attackIndex -= 2
                    if event.key == pygame.K_a:
                        playerPokemonOut.attack(enemyPokemonOut)
                        animation.x = 50
                        animation.y = 300
                        enemyAnimation.x = 550
                        enemyAnimation.y = 25
                        time = 0
                        enemyAttackIndex = randint(0, 3)

        # if time > 180:
        #     if GPIO.input(18) == 1:
        #         attackIndex -= 1
        #         sleep(.3)
        #     elif gpio.input(19) == 1:
        #         attackIndex += 1
        #         sleep(.3)
        #     elif GPIO.input(20) == 1:
        #         attackIndex -= 4
        #         sleep(.3)
        #     elif gpio.input(21) == 1:
        #         attackIndex += 4
        #         sleep(.3)
        #     elif gpio.imput(22) == 1:
        #         p1.attack(p2)
        #         animation.x = 50
        #         animation.y = 300
        #         enemyAnimation.x = 550
        #         enemyAnimation.y = 25
        #         time = 0
        #         enemyAttackIndex = randint(0,3)

        if time < 90:
            displayAnimation(animation, playerPokemonOut, attackIndex)
        elif time < 180:
            displayEnemyAnimation(enemyAnimation, enemyPokemonOut, enemyAttackIndex)
        displayText(playerPokemonOut, enemyPokemonOut, attackIndex, time, enemyAttackIndex)
        displayEnenmy(enemyPokemonOut)
        displayPlayer(playerPokemonOut.img)
        displayHealth(playerPokemonOut, enemyPokemonOut)
        # displaySpriteNames()
        displayMoves(playerPokemonOut, enemyPokemonOut, attackIndex)
        determineDeath(playerPokemonOut, enemyPokemonOut)
        drawScreen()

        if (p1p1.health <= 0):
            playerPokemonOut = p1p2
        if (p1p2.health <= 0):
            playerPokemonOut = p1p3
        if (p2p1.health <= 0):
            enemyPokemonOut = p2p2
        if (p2p2.health <= 0):
            enemyPokemonOut = p2p3
        if (p1p3.health <= 0):
            winner = enemyIndexList
            return winner
            run = False
        if (p2p3.health <= 0):
            winner = choiceIndexList
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
        screen.blit(winner[0].img, (300, 100))
        drawScreen()


# Main Code
choiceIndexList = menuLoop()
winner = gameLoop(choiceIndexList)
victoryLoop(winner)
