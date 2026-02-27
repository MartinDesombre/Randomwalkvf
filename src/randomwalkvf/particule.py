import random

class Particule:
    def __init__(self, position: tuple, color):
        self.position = list(position)
        self.color = color
        self.path = [tuple(self.position)]
        
    
    def move(self):

        # on choisit une direction aléatoire parmi les 4 possibles et on met a jour la position de la particule en ajoutant cette direction

        direction = random.randint(0,3)
        if direction == 0:
            self.position[0] += 1
        elif direction == 1:
            self.position[0] -= 1
        elif direction == 2:
            self.position[1] += 1
        else:
            self.position[1] -= 1
        self.path.append(tuple(self.position))