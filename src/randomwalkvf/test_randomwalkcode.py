import os
import pytest
import pygame
from randomwalkcode import Particule, Simulation

def test_particule_init(): #pour verifiquer que la particule est bien initialisée
    p = Particule((0, 0), pygame.Color("red"))
    assert p.position == [0, 0]
    assert p.path == [(0, 0)]
    assert p.color == pygame.Color("red")

def test_particule_move():  #pour verifier que la particule bouge et que son chemin est mis à jour
    p = Particule((0, 0), (255, 0, 0))
    p.move()
    assert len(p.path) == 2 #le chemin doit contenir la position initiale et la nouvelle position
    x, y = p.position
    assert (abs(x) == 1 and y == 0) or (x == 0 and abs(y) == 1) #on verifie que la particule a bougé d'une seule case

def test_simulation_chemin_sans_affichage():  #pour verifier que le nombre d'étapes est respecté
    sim = Simulation(nb_particules=2, steps=5)
    sim.chemin_sans_affichage()
    for p in sim.particules:
        assert len(p.path) == 6 #on verifie qu'il y a la position initiale+5 nouvelles positions

