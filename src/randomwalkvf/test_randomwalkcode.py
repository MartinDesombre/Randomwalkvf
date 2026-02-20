import os
import pytest
import pygame
from randomwalkcode import Particule, Simulation

def test_particule_move():  #pour verifier que la particule bouge et que son chemin est mis à jour
    p = Particule((0, 0), (255, 0, 0))
    p.move()
    assert len(p.path) == 2 #le chemin doit contenir la position initiale et la nouvelle position
    x, y = p.position
    assert (abs(x) == 1 and y == 0) or (x == 0 and abs(y) == 1) #on verifie que la particule a bougé d'une seule case

