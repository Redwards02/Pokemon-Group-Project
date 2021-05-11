import time
import pygame

#sprites
abombImg = pygame.image.load('abomb.png')
gelatorImg = pygame.image.load('gelator.png')
kroakenImg = pygame.image.load('kroaken.png')
ericImg = pygame.image.load('eric.png')
nachosImg = pygame.image.load('nachos.png')
brickdoopImg = pygame.image.load('brickdoop.png')
bottlerockerImg = pygame.image.load('bottlerocker.png')
dracolichImg = pygame.image.load('dracolich.png')
arrowImg = pygame.image.load('arrow.png')

#animations
rockImg = pygame.image.load("rock.png")

class Pokemon:
    def __init__(self, name, types, atk, defense, health, img):
        self.name = name
        self.types = types
        self.atk = atk
        self.defense = defense
        self.health = health
        self.img = img

    def attack(self, Pokemon2):
        # type advantages
        pTypes = ['Fire', 'Water', 'Grass', 'Ghost', 'Psychic', 'Rock', 'Flying', 'Dragon']
        # fire type
        if self.types == pTypes[0]:
            # weak against water
            if Pokemon2.types == pTypes[1]:
                Pokemon2.atk *= 2
                Pokemon2.defense *= 2
                self.atk /= 2
                self.defense /= 2
            # strong against grass
            elif Pokemon2.types == pTypes[2]:
                Pokemon2.atk /= 2
                Pokemon2.defense /= 2
                self.atk *= 2
                self.defense *= 2
            # weak agaisnt rock
            elif Pokemon2.types == pTypes[5]:
                Pokemon2.atk *= 2
                Pokemon2.defense *= 2
                self.atk /= 2
                self.defense /= 2
            # weak attack against dragon
            elif Pokemon2.types == pTypes[7]:
                self.atk /= 2
        # water type
        elif self.types == pTypes[1]:
            # strong against fire
            if Pokemon2.types == pTypes[0]:
                Pokemon2.atk /= 2
                Pokemon2.defense /= 2
                self.atk *= 2
                self.defense *= 2
            # weak against grass
            elif Pokemon2.types == pTypes[2]:
                Pokemon2.atk *= 2
                Pokemon2.defense *= 2
                self.atk /= 2
                self.defense /= 2
            # strong against rock
            elif Pokemon2.types == pTypes[5]:
                Pokemon2.atk /= 2
                Pokemon2.defense /= 2
                self.atk *= 2
                self.defense *= 2
            # weak attack vs dragon
            elif Pokemon2.types == pTypes[7]:
                self.atk /= 2
        # grass
        elif self.types == pTypes[2]:
            # weak against fire
            if Pokemon2.types == pTypes[0]:
                Pokemon2.atk *= 2
                Pokemon2.defense *= 2
                self.atk /= 2
                self.defense /= 2
            # strong vs water
            elif Pokemon2.types == pTypes[1]:
                Pokemon2.atk /= 2
                Pokemon2.defense /= 2
                self.atk *= 2
                self.defense *= 2
            # strong vs rock
            elif Pokemon2.types == pTypes[5]:
                Pokemon2.atk /= 2
                Pokemon2.defense /= 2
                self.atk *= 2
                self.defense *= 2
            # weak vs flying
            elif Pokemon2.types == pTypes[6]:
                Pokemon2.atk *= 2
                Pokemon2.defense *= 2
                self.atk /= 2
                self.defense /= 2
            # weak atk vs dragon
            elif Pokemon2.types == pTypes[7]:
                self.atk /= 2
        # ghost
        elif self.types == pTypes[3]:
            # strong vs self
            if Pokemon2.types == pTypes[3]:
                Pokemon2.atk *= 2
                Pokemon2.defense /= 2
                self.atk *= 2
                self.defense /= 2
            # strong atk vs psychic
            elif Pokemon2.types == pTypes[4]:
                self.atk *= 2
        # psychic
        elif self.types == pTypes[4]:
            # weak defense vs ghost
            if Pokemon2.types == pTypes[3]:
                Pokemon2.defense /= 2

        # rock
        elif self.types == pTypes[5]:
            # strong vs fire
            if Pokemon2.types == pTypes[0]:
                Pokemon2.atk /= 2
                Pokemon2.defense /= 2
                self.atk *= 2
                self.defense *= 2
            # weak def vs water
            elif Pokemon2.types == pTypes[1]:
                self.defense /= 2
            # strong vs flying
            elif Pokemon2.types == pTypes[6]:
                Pokemon2.atk /= 2
                Pokemon2.defense /= 2
                self.atk *= 2
                self.defense *= 2

        # flying
        elif self.types == pTypes[6]:
            # strong vs grass
            if Pokemon2.types == pTypes[2]:
                Pokemon2.atk /= 2
                Pokemon2.defense /= 2
                self.atk *= 2
                self.defense *= 2
            # weak vs rock
            elif Pokemon2.types == pTypes[5]:
                Pokemon2.atk *= 2
                Pokemon2.defense *= 2
                self.atk /= 2
                self.defense /= 2

        # dragon
        elif self.types == pTypes[7]:
            # strong def vs fire
            if Pokemon2.types == pTypes[0]:
                self.defense *= 2
            # strong def vs water
            elif Pokemon2.types == pTypes[1]:
                self.defense *= 2
            # strong def vs grass
            elif Pokemon2.types == pTypes[2]:
                self.defense *= 2
            # weak vs self
            Pokemon2.atk *= 2
            Pokemon2.defense /= 2
            self.atk *= 2
            self.defense /= 2

        Pokemon2.health -= self.atk / Pokemon2.defense
        return Pokemon2.health

class Nabomb(Pokemon):
    def __init__(self,name = 'Nabomb', types='Fire', atk=30, defense=3, health=50, img = abombImg, moveNames = ["Fireball", "Flamethrower", "Atomic Cherry Bomb", "Fiery Inferno"], moveImgs = ["FireBall.png", "Flamethrower.png","AtomicCherriBomb.png","FieryInferno.png"]):
        Pokemon.__init__(self, name, types, atk, defense, health, img)
        self.moveNames = moveNames
        self.moveImgs = moveImgs

    def getText(self, attackIndex):
        if attackIndex == 0:
            return "Nabomb used Fireball"
        elif attackIndex == 1:
            return "Nabomb used Flamethrower"
        elif attackIndex == 2:
            return "Nabomb used Atomic Cherry Bomb"
        elif attackIndex == 3:
            return "Nabomb used Fiery Inferno"

    def getDescription(self):
        return "Watch out! He might go off!"

class Gelator(Pokemon):
    def __init__(self, name = "Gelator", types='Water', atk=30, defense=3, health=50, img = gelatorImg, moveNames = ["Water Gun", "Gelatinous Wave", "Lime Jelly Power", "JelliBomb"],moveImgs = ['WaterGun.png', 'GelatnousWave.png','LimeJellyPower.png','JelliBomb.png']):
        Pokemon.__init__(self,name, types, atk, defense, health, img)
        self.moveNames = moveNames
        self.moveImgs = moveImgs
    def getText(self, attackIndex):
        if attackIndex == 0:
            return "Gelator used Water Gun"
        elif attackIndex == 1:
            return "Gelator used Gelatinous Wave"
        elif attackIndex == 2:
            return "Gelator used Lime Jelly Power"
        elif attackIndex == 3:
            return "Gelator used JelliBomb"

    def getDescription(self):
        return "He is blue rasberry flavor!"

class Kroaken(Pokemon):
    def __init__(self,name = 'Kroaken', types='Grass', atk=30, defense=5, health=50, img = kroakenImg, moveNames = ["Vine Whip", "Pine Cone Throw", "Oaky Venom", "Log Smash"], moveImgs =['VineWhip.png','PineConeThrow.png','OakyVenom.png','LogSmash.png'], ballImg = "KroakenBall.png"):
        Pokemon.__init__(self, name,types, atk, defense, health, img)
        self.ballImg = ballImg
        self.moveNames = moveNames
        self.moveImgs = moveImgs

    def getText(self, attackIndex):
        if attackIndex == 0:
            return "Kroaken used Vine Whip"
        elif attackIndex == 1:
            return "Kroaken used Pine Cone Throw"
        elif attackIndex == 2:
            return "Kroaken used Oaky Venom"
        elif attackIndex == 3:
            return "Kroaken used Log Smash"

    def getDescription(self):
        return "A kraken that has rooted itself!"

class Eric(Pokemon):
    def __init__(self,name = 'Eric', types='Ghost', atk=30, defense=1, health=50, img = ericImg, moveNames = ["Spirit Bomb", "Absentee Father", "Caspers Revenge", "Spooky Mist"], moveImgs = ['SpiritBomb.png', 'AbsentFather.png','CaspersRevenge.png','SpookyMist.png']):
        Pokemon.__init__(self,name, types, atk, defense, health, img)
        self.moveNames = moveNames
        self.moveImgs = moveImgs
    def getText(self, attackIndex):
        if attackIndex == 0:
            return "Eric used Spirit Bomb"
        elif attackIndex == 1:
            return "Eric used Absentee Father"
        elif attackIndex == 2:
            return "Eric used Caspers Revenge"
        elif attackIndex == 3:
            return "Eric used Spooky Mist"

    def getDescription(self):
        return "Had a rough life, not much to say"

class Nachos(Pokemon):
    def __init__(self,name = 'Nachos', types='Psychic', atk=30, defense=5, health=50, img = nachosImg, moveNames = ["Tortilla Shuriken","Cheesy Chips", "Nuke Bell Grande", "Spicy Jalepeno Surprise"],moveImgs = ['TortillaShuriken.png','CheesyChips.png','NukeBellGrande.png','SpicyJalepenoSuprise.png']):
        Pokemon.__init__(self,name, types, atk, defense, health, img)
        self.moveNames = moveNames
        self.moveImgs = moveImgs

    def getText(self, attackIndex):
        if attackIndex == 0:
            return "Nachos used Tortilla Shuriken"
        elif attackIndex == 1:
            return "Nachos used Cheesy Chips"
        elif attackIndex == 2:
            return "Nachos used Nuke Bell Grande"
        elif attackIndex == 3:
            return "Nachos used Spicy Jalepeno Surprise"
    def getDescription(self):
        return "His favorite food in the world is nachos!"

class Brickdoop(Pokemon):
    def __init__(self,name = 'Brickdoop', types='Rock', atk=30, defense=3, health=50, img = brickdoopImg, moveNames = ["Brick Throw", "Big Brick", "Brick Bomb", "Brick Smash"], moveImgs = ['BrickThrow.png','BigBrick.png','BrickBomb.png','BrickSmash.png']):
        Pokemon.__init__(self,name, types, atk, defense, health, img)
        self.moveNames = moveNames
        self.moveImgs = moveImgs

    def getText(self, attackIndex):
        if attackIndex == 0:
            return "Brickdoop used Brick Throw"
        elif attackIndex == 1:
            return "Brickdoop used Big Brick"
        elif attackIndex == 2:
            return "Brickdoop used Brick Bomb"
        elif attackIndex == 3:
            return "Brickdoop used Brick Smash"

    def getDescription(self):
        return "Watch out hes got a brick!"

class Bottlerocker(Pokemon):
    def __init__(self, name = 'Bottlerocker', types='Flying', atk=30, defense=6, health=50, img = bottlerockerImg, moveNames = ["Big Bang", "Gust", "Supersonic Boom", "Air Strike"], moveImgs = ['BigBang.png','Gust.png','SonicBoom.png','AirStrike.png']):
        Pokemon.__init__(self,name, types, atk, defense, health, img)
        self.moveNames = moveNames
        self.moveImgs = moveImgs

    def getText(self, attackIndex):
        if attackIndex == 0:
            return "Bottlerocker used Big Bang"
        elif attackIndex == 1:
            return "Bottlerocker used Gust"
        elif attackIndex == 2:
            return "Bottlerocker used Supersonic Boom"
        elif attackIndex == 3:
            return "Bottlerocker used Air Strike"

    def getDescription(self):
        return "A firework with a personality!"

class Dracolich(Pokemon):
    def __init__(self,name = 'Dracolich', types='Dragon', atk=30, defense=4, health=50, img = dracolichImg, moveNames = ["Dragon Dance", "Fire Breath", "Dragon Hammer", "Desolation of Smaug"], moveImgs = ['DragonDance.png', 'FireBreath.png','DragonHammer.png','DesolationOfSmough.png']):
        Pokemon.__init__(self,name, types, atk, defense, health, img)
        self.moveNames = moveNames
        self.moveImgs = moveImgs

    def getText(self, attackIndex):
        if attackIndex == 0:
            return "Dracolich used Dragon Dance"
        elif attackIndex == 1:
            return "Dracolich used Fire Breath"
        elif attackIndex == 2:
            return "Dracolich used Dragon Hammer"
        elif attackIndex == 3:
            return "Dracolich used Desolation of Smaug"

    def getDescription(self):
        return "A dragon that has risen from the dead!"
        
