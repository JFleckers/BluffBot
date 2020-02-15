import random

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
