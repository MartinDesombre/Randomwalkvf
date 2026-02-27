import random

class Particule:
    """cette classe représente une particule dans la simulation, elle a une position, une couleur et un chemin qui stocke toutes les positions qu'elle a occupées pendant la simulation"""
    def __init__(self, position: tuple, color):
        """initialise la particule avec une position, une couleur et un chemin qui contient la position initiale"""
        self.position = list(position)
        self.color = color
        self.path = [tuple(self.position)]
        
    
    def move(self):

        """fait bouger la particule d'une case dans une direction aléatoire et ajoute la nouvelle position à son chemin"""

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