import pygame
from randomwalkvf.particule import Particule

class Simulation(): 
    def __init__(self, nb_particules: int, steps: int):
        self.particules = []
        #on crée les particules en leur attribuant une couleur différente pour chacune en utilisant des teintes reparties sur l'arc en ciel
        for i in range(nb_particules):
            c = pygame.Color(0, 0, 0)
            hue = (360 * i) / nb_particules      #repartition uniforme des teintes sur l'arc en ciel
            c.hsva = (hue, 100, 100, 100)
            self.particules.append(Particule((0, 0), c,))
        self.steps_totaux = steps

    #si gui pas activé on faut bouger les particules sans afficher le chemin
    def chemin_sans_affichage(self):  
        for i in range(self.steps_totaux):
            for particule in self.particules:
                particule.move()
        print(f"Calcul de {self.steps_totaux} étapes terminé")

    #si gui activé on affiche le chemin de chaque particule à chaque étape
    #on adapte aussi le zoom pour que toutes les particules soient visibles


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

            #on va calculer le min et max des coordonnées des particules pour ensuite adapter le zoom avec le facteur scale

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

        #on affiche le chemin de chaque particule en reliant les points de son chemin avec des lignes de la couleur de la particule

            screen.fill((0, 0, 0))
            for particule in self.particules:
                points = [transform(x, y) for x, y in particule.path]    #nouvelles coordonnées
                if len(points) > 1:
                    pygame.draw.lines(screen, particule.color, False, points, 2)
            
        #on affiche le nombre d'étapes réalisées en haut à gauche de la fenetre

            text_surface = font.render(f"Step: {current_step} / {self.steps_totaux}",True,(255, 255, 255)) #on met a jour le nombre d'étapes
            screen.blit(text_surface, (10, 10))
            pygame.display.flip()
             #fps images par seconde
            clock.tick(fps)

    #on écrit dans le fichier toutes les étapes des particules en parcourant son path

    def ecrire_fichier(self, filename: str):  
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"--- États pour {self.steps_totaux} étapes ---\n")
            for i, particule in enumerate(self.particules):
                x, y = particule.position
                f.write(f"Particule {i+1} : x={x}, y={y}\n")
                for etape, position in enumerate(particule.path):
                    f.write(f"  Étape {etape} : x={position[0]}, y={position[1]}\n")
        
        print(f"L'historique des états a été sauvegardé dans '{filename}'")
        pygame.quit()


#remarques: on a parfois l'impression que les particules ne se deplacent pas depuis le dernier endroit ou elles ont été
# mais aussi depuis d'autres endroits sur leur chemin, c'est du au zoom auto