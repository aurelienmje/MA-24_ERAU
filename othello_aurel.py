import pygame
from tkinter.messagebox import *

# DÉFINITION DES VARIABLES :

color_circle = (0, 0, 0)
cpt = 60

# PRÉPARATION DE PYGAME ET DE LA FENÊTRE

pygame.init()

screen = pygame.display.set_mode((890,890))
screen.fill((0,128,0))

pygame.display.set_caption("MA-24 : Bases de pygame")


# DÉFINITION DES CASES :

compteur = 0
posx = 10
cases = []
for case in range(64):
    posy = 10
    for column in range(8):
        if compteur == 27 or compteur == 36:
            cases = cases + [[pygame.draw.rect(screen, (0, 104, 0), (posx, posy, 100, 100), border_radius=20), 1]]
            posy = posy + 110
        elif compteur == 28 or compteur == 35:
            cases = cases + [[pygame.draw.rect(screen, (0, 104, 0), (posx, posy, 100, 100), border_radius=20), 2]]
            posy = posy + 110
        else:
            cases = cases + [[pygame.draw.rect(screen, (0, 104, 0), (posx, posy, 100, 100), border_radius=20), 0]]
            posy = posy + 110
        compteur = compteur + 1
    posx = posx + 110
print(cases)
print(cases[28][1])

for cercle in cases:
    if cercle[1] == 1:
        pygame.draw.circle(screen, (255, 255, 255), cercle[0].center, 45)
    elif cercle[1] == 2:
        pygame.draw.circle(screen, (0, 0, 0), cercle[0].center, 45)

# AFFICHAGE DES ÉLÉMENTS :

pygame.display.update()

# BOUCLE RUNNING :

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for i in cases:
                if i[0].collidepoint(pos):
                    if i[1] > 0:
                        print('Impossible')
                    else:
                        cpt = cpt - 1
                        print(cpt)
                        if color_circle == (255, 255, 255):
                            pygame.draw.circle(screen, color_circle, i[0].center, 45)
                            color_circle = (0, 0, 0)
                            i = i[0], 1
                        elif color_circle == (0, 0, 0):
                            pygame.draw.circle(screen, color_circle, i[0].center, 45)
                            color_circle = (255, 255, 255)
                            i = i[0], 2
                        print(f"Position du clic : {pos}\nPion posé à {i[0]}\n")
                        update = 0
                        for test in cases:
                            if i[0] == test[0]:
                                cases[update][1] = i[1]
                            else:
                                update = update + 1

                    if cpt == 0:
                        showinfo(title="Fin du jeu !", message="Le jeu est fini, toutes les cases sont remplies !")
            pygame.display.update()

        if event.type == pygame.QUIT:
            running = False

pygame.quit()