import pygame

# DÉFINITION DES VARIABLES :

color_circle = (0, 0, 0)

# PRÉPARATION DE PYGAME ET DE LA FENÊTRE

pygame.init()

screen = pygame.display.set_mode((890,890))
screen.fill((0,128,0))

pygame.display.set_caption("MA-24 : Bases de pygame")

# DÉFINITION DES CASES :

def dessiner_cases():
    compteur = 0
    posx = 10
    cases = []
    for case in range(8):
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

    for cercle in cases:
        if cercle[1] == 1:
            pygame.draw.circle(screen, (255, 255, 255), cercle[0].center, 45)
        elif cercle[1] == 2:
            pygame.draw.circle(screen, (0, 0, 0), cercle[0].center, 45)

    pygame.display.update()
    return cases

cases = dessiner_cases()