class Pokemon:
    def __init__(self, typing, health):
        self.typing = typing
        self.moves = moves

    # moves all pokemon have

    def headbutt(self):
        pass

    def pound(self):
        pass

    # types and type specific moves


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
    def __init__(self, attack, defense, spAttack, spDefense, health, speed):
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
