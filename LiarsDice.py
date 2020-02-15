import random

class Game:
    def __init__(self,pCount):
        self.turn
        self.state
        self.pCount = pCount

class Player:
    def __init__(self,name):
        self.pCup = Cup()
        self.name = name
        
class Die:
    def __init__(self):
        self.die = random.randint(1,6)
    
class Cup:    
    
    def __init__(self):
        self.cup = []
        self.count = 5
        
    def roll(self):
        self.cup.clear()
        x = 0
        while x <= 5:
            self.cup.append(Die())
            x += 1
    
    def lose(self):
        self.count -= 1