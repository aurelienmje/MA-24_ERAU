import pygame
import menu
from menu import *
from tkinter.messagebox import *
import gfx

cpt = 60

# BOUCLE RUNNING :

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for i in gfx.cases:
                if i[0].collidepoint(pos):
                    if i[1] > 0:
                        print('Impossible')
                    else:
                        cpt = cpt - 1
                        if gfx.color_circle == (255, 255, 255):
                            cercle = pygame.draw.circle(gfx.screen, gfx.color_circle, i[0].center, 45)
                            gfx.color_circle = (0, 0, 0)
                            i = i[0], 1
                        elif gfx.color_circle == (0, 0, 0):
                            pygame.draw.circle(gfx.screen, gfx.color_circle, i[0].center, 45)
                            gfx.color_circle = (255, 255, 255)
                            i = i[0], 2

                        update = 0
                        for n in gfx.cases:
                            if i[0] == n[0]:
                                gfx.cases[update][1] = i[1]
                            else:
                                update = update + 1

            pygame.display.update()
            if cpt == 0:
                showinfo(title="Fin du jeu !", message="Le jeu est fini, toutes les cases sont remplies !")
                gfx.cases = gfx.dessiner_cases()

        if event.type == pygame.QUIT:
            running = False

pygame.quit()