import os
import pytest
import pygame
from unittest.mock import patch
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

def test_ecrire_fichier(tmp_path):   #on vérifie que le fichier de sortie est bien créé
    sim = Simulation(nb_particules=1, steps=2)
    fichier_test = tmp_path / "test_output.txt"
    sim.ecrire_fichier(str(fichier_test))
    assert os.path.exists(fichier_test)

def test_afficher_chemin_fermeture_immediate():    
    os.environ["SDL_VIDEODRIVER"] = "dummy"  # on coupe l'affichage visuel pour que le test ne plante pas
    sim = Simulation(nb_particules=2, steps=2)
    with patch('pygame.event.get') as mock_event_get:      # On simule la fermeture instantanée de la fenetre
        mock_event_get.return_value = [pygame.event.Event(pygame.QUIT)]
        sim.afficher_chemin(fps=60)
    del os.environ["SDL_VIDEODRIVER"]
    #cette fonction je ne savais pas la faire tout seul... c'était pour dépasser 60% de coverage (avant son ecriture j'etais a 44%)