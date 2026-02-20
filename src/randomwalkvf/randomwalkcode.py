import random
import pygame
import argparse

def main() -> None:
    parser = argparse.ArgumentParser(description="Simulate random walk for particles.")
    parser.add_argument("-N","--nb-particules", type=int, required=False, default=1, metavar="INTEGER",help="Number of particles")
    parser.add_argument("-n","--nb-steps", type=int, required=False, default=100, metavar="INTEGER",help="Number of steps until end of simulation")
    parser.add_argument("--fps", type=int, default=5, metavar="INTEGER",help="The number of frames per second")
    parser.add_argument("-o", "--output", type=str, default="finalstate.txt", metavar="FILENAME",help="The file with the final state of the grid.")
    parser.add_argument("-x", "--gui", action="store_true", help="Activate the pygame interface")

    args = parser.parse_args()
    sim = Simulation(args.nb_particules, args.nb_steps)
    if args.gui:
        print("Mode GUI activé. Fermez la fenêtre pour sauvegarder le fichier.")
        sim.afficher_chemin(fps=args.fps)
    else:
        print("Mode silencieux (sans interface). Calcul en cours...")
        sim.chemin_sans_affichage()

    sim.ecrire_fichier(args.output)


class Particule:
    def __init__(self, position: tuple, color):
        self.position = list(position)
        self.color = color
        self.path = [tuple(self.position)]
    
    def move(self):
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
    


class Simulation(): 
    def __init__(self, nb_particules: int, steps: int):
        self.particules = []
        for i in range(nb_particules):
            c = pygame.Color(0, 0, 0)
            hue = (360 * i) / nb_particules       #on l'utilise pour avoir toujours des couleurs différentes
            c.hsva = (hue, 100, 100, 100)
            self.particules.append(Particule((0, 0), c))
        
        self.steps_totaux = steps

    def chemin_sans_affichage(self):  # si gui pas activé
        for i in range(self.steps_totaux):
            for particule in self.particules:
                particule.move()
        print(f"Calcul de {self.steps_totaux} étapes terminé")

    def afficher_chemin(self, fps: int):
        pygame.init()
        pygame.font.init()
        width, height = 800, 600
        screen = pygame.display.set_mode((width, height))
        running = True
        current_step = 0
        clock = pygame.time.Clock()
        font = pygame.font.SysFont(None, 36)
        print("Affichage lancé")
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if current_step < self.steps_totaux:
                for particule in self.particules:
                    particule.move()
                current_step += 1
            all_x = [p[0] for part in self.particules for p in part.path]
            all_y = [p[1] for part in self.particules for p in part.path]
            min_x, max_x = min(all_x), max(all_x)
            min_y, max_y = min(all_y), max(all_y)
            delta_x = max_x - min_x
            delta_y = max_y - min_y
            coef = 0.9
            if delta_x!=0 and delta_y!=0:
                scale = min((width * coef) / delta_x, (height * coef) / delta_y)    #on dezoome pour voir toutes les particules
            else:
                scale = 1

        #il nous reste à adapter les coordonnées de chaque particule à la nouvelle échelle
            def transform(x, y):
                screen_x = int((x - (min_x + max_x) / 2) * scale + width / 2)
                screen_y = int(-(y - (min_y + max_y) / 2) * scale + height / 2)
                return (screen_x, screen_y)

            screen.fill((0, 0, 0))
            for particule in self.particules:
                points = [transform(x, y) for x, y in particule.path]    #nouvelles coordonnées
                if len(points) > 1:
                    pygame.draw.lines(screen, particule.color, False, points, 2)
            
            text_surface = font.render(f"Step: {current_step} / {self.steps_totaux}",True,(255, 255, 255)) #on met a jour le nombre d'étapes
            screen.blit(text_surface, (10, 10))
            pygame.display.flip()
             #5 images par seconde
            clock.tick(fps)
        def ecrire_fichier(self, filename: str):  #on écrit dans le fichier l'état final de chaque particule
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"--- État final après {self.steps_totaux} étapes ---\n")
            for i, particule in enumerate(self.particules):
                x, y = particule.position
                f.write(f"Particule {i+1} : x={x}, y={y}\n")
        
        print(f"L'état final a été sauvegardé dans '{filename}'")
        pygame.quit()




#remarques: on a parfois l'impression que les particules ne se deplacent pas depuis le dernier endroit ou elles ont été
# mais aussi depuis d'autres endroits sur leur chemin, c'est du au zoom auto
