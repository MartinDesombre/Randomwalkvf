import argparse
from randomwalkvf.simulation import Simulation

#on définit les differents arguments que le programme peut prendre et que l'utilisateur doit renseigner
#si l'utilisateur ne les renseigne pas, on utilise des valeurs par défaut, on n'affiche pas la fenetre pygame et on nomme le texte de sortie finalstate.txt

def main() -> None:
    """fonction principale qui gère les arguments de la ligne de commande, lance la simulation et écrit les résultats dans un fichier texte"""
    
    parser = argparse.ArgumentParser(description="Simulate random walk for particles.", add_help=False)
    parser.add_argument("-h", "--help", action="help", default=argparse.SUPPRESS, help="Vous pouvez simuler une marche aléatoire de N particules pendant n étapes, avec ou sans interface graphique et stocker la position finale dans un fichier texte.")
    parser.add_argument("-N","--nb-particules", type=int, required=False, default=1, metavar="INTEGER",help="Number of particles")
    parser.add_argument("-n","--nb-steps", type=int, required=False, default=100, metavar="INTEGER",help="Number of steps until end of simulation")
    parser.add_argument("--fps", type=int, default=5, metavar="INTEGER",help="The number of frames per second")
    parser.add_argument("-o", "--output", type=str, default="finalstate.txt", metavar="FILENAME",help="The file with the final state of the grid.")
    parser.add_argument("-x", "--gui", action="store_true", help="Activate the pygame interface")

    args = parser.parse_args()
    sim = Simulation(args.nb_particules, args.nb_steps)

    #ici on distingue le cas ou l'utilisateur souhaite une interface graphique de celui ou il ne la souhaite pas

    if args.gui:
        print("Mode GUI activé. Fermez la fenêtre pour sauvegarder le fichier.")
        sim.afficher_chemin(fps=args.fps)
    else:
        print("Mode silencieux (sans interface). Calcul en cours...")
        sim.chemin_sans_affichage()
    #dans tous les cas on écrit le résultat des etats dans un fichier texte
    sim.ecrire_fichier(args.output)






