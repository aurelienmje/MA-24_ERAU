import pygame

# DÉFINITION DES VARIABLES :

color_circle = (0, 0, 0)

# PRÉPARATION DE PYGAME ET DE LA FENÊTRE

pygame.init()

screen = pygame.display.set_mode((890,890))
screen.fill((0,128,0))

pygame.display.set_caption("MA-24 : Bases de pygame")


# DÉFINITION DES CASES :

a1 = pygame.draw.rect(screen, (0, 104, 0), (10, 10, 100, 100), border_radius=20)
a2 = pygame.draw.rect(screen, (0, 104, 0), (10, 120, 100, 100), border_radius=20)
a3 = pygame.draw.rect(screen, (0, 104, 0), (10, 230, 100, 100), border_radius=20)
a4 = pygame.draw.rect(screen, (0, 104, 0), (10, 340, 100, 100), border_radius=20)
a5 = pygame.draw.rect(screen, (0, 104, 0), (10, 450, 100, 100), border_radius=20)
a6 = pygame.draw.rect(screen, (0, 104, 0), (10, 560, 100, 100), border_radius=20)
a7 = pygame.draw.rect(screen, (0, 104, 0), (10, 670, 100, 100), border_radius=20)
a8 = pygame.draw.rect(screen, (0, 104, 0), (10, 780, 100, 100), border_radius=20)
b1 = pygame.draw.rect(screen, (0, 104, 0), (120, 10, 100, 100), border_radius=20)
b2 = pygame.draw.rect(screen, (0, 104, 0), (120, 120, 100, 100), border_radius=20)
b3 = pygame.draw.rect(screen, (0, 104, 0), (120, 230, 100, 100), border_radius=20)
b4 = pygame.draw.rect(screen, (0, 104, 0), (120, 340, 100, 100), border_radius=20)
b5 = pygame.draw.rect(screen, (0, 104, 0), (120, 450, 100, 100), border_radius=20)
b6 = pygame.draw.rect(screen, (0, 104, 0), (120, 560, 100, 100), border_radius=20)
b7 = pygame.draw.rect(screen, (0, 104, 0), (120, 670, 100, 100), border_radius=20)
b8 = pygame.draw.rect(screen, (0, 104, 0), (120, 780, 100, 100), border_radius=20)
c1 = pygame.draw.rect(screen, (0, 104, 0), (230, 10, 100, 100), border_radius=20)
c2 = pygame.draw.rect(screen, (0, 104, 0), (230, 120, 100, 100), border_radius=20)
c3 = pygame.draw.rect(screen, (0, 104, 0), (230, 230, 100, 100), border_radius=20)
c4 = pygame.draw.rect(screen, (0, 104, 0), (230, 340, 100, 100), border_radius=20)
c5 = pygame.draw.rect(screen, (0, 104, 0), (230, 450, 100, 100), border_radius=20)
c6 = pygame.draw.rect(screen, (0, 104, 0), (230, 560, 100, 100), border_radius=20)
c7 = pygame.draw.rect(screen, (0, 104, 0), (230, 670, 100, 100), border_radius=20)
c8 = pygame.draw.rect(screen, (0, 104, 0), (230, 780, 100, 100), border_radius=20)
d1 = pygame.draw.rect(screen, (0, 104, 0), (340, 10, 100, 100), border_radius=20)
d2 = pygame.draw.rect(screen, (0, 104, 0), (340, 120, 100, 100), border_radius=20)
d3 = pygame.draw.rect(screen, (0, 104, 0), (340, 230, 100, 100), border_radius=20)
d4 = pygame.draw.rect(screen, (0, 104, 0), (340, 340, 100, 100), border_radius=20)
d5 = pygame.draw.rect(screen, (0, 104, 0), (340, 450, 100, 100), border_radius=20)
d6 = pygame.draw.rect(screen, (0, 104, 0), (340, 560, 100, 100), border_radius=20)
d7 = pygame.draw.rect(screen, (0, 104, 0), (340, 670, 100, 100), border_radius=20)
d8 = pygame.draw.rect(screen, (0, 104, 0), (340, 780, 100, 100), border_radius=20)
e1 = pygame.draw.rect(screen, (0, 104, 0), (450, 10, 100, 100), border_radius=20)
e2 = pygame.draw.rect(screen, (0, 104, 0), (450, 120, 100, 100), border_radius=20)
e3 = pygame.draw.rect(screen, (0, 104, 0), (450, 230, 100, 100), border_radius=20)
e4 = pygame.draw.rect(screen, (0, 104, 0), (450, 340, 100, 100), border_radius=20)
e5 = pygame.draw.rect(screen, (0, 104, 0), (450, 450, 100, 100), border_radius=20)
e6 = pygame.draw.rect(screen, (0, 104, 0), (450, 560, 100, 100), border_radius=20)
e7 = pygame.draw.rect(screen, (0, 104, 0), (450, 670, 100, 100), border_radius=20)
e8 = pygame.draw.rect(screen, (0, 104, 0), (450, 780, 100, 100), border_radius=20)
f1 = pygame.draw.rect(screen, (0, 104, 0), (560, 10, 100, 100), border_radius=20)
f2 = pygame.draw.rect(screen, (0, 104, 0), (560, 120, 100, 100), border_radius=20)
f3 = pygame.draw.rect(screen, (0, 104, 0), (560, 230, 100, 100), border_radius=20)
f4 = pygame.draw.rect(screen, (0, 104, 0), (560, 340, 100, 100), border_radius=20)
f5 = pygame.draw.rect(screen, (0, 104, 0), (560, 450, 100, 100), border_radius=20)
f6 = pygame.draw.rect(screen, (0, 104, 0), (560, 560, 100, 100), border_radius=20)
f7 = pygame.draw.rect(screen, (0, 104, 0), (560, 670, 100, 100), border_radius=20)
f8 = pygame.draw.rect(screen, (0, 104, 0), (560, 780, 100, 100), border_radius=20)
g1 = pygame.draw.rect(screen, (0, 104, 0), (670, 10, 100, 100), border_radius=20)
g2 = pygame.draw.rect(screen, (0, 104, 0), (670, 120, 100, 100), border_radius=20)
g3 = pygame.draw.rect(screen, (0, 104, 0), (670, 230, 100, 100), border_radius=20)
g4 = pygame.draw.rect(screen, (0, 104, 0), (670, 340, 100, 100), border_radius=20)
g5 = pygame.draw.rect(screen, (0, 104, 0), (670, 450, 100, 100), border_radius=20)
g6 = pygame.draw.rect(screen, (0, 104, 0), (670, 560, 100, 100), border_radius=20)
g7 = pygame.draw.rect(screen, (0, 104, 0), (670, 670, 100, 100), border_radius=20)
g8 = pygame.draw.rect(screen, (0, 104, 0), (670, 780, 100, 100), border_radius=20)
h1 = pygame.draw.rect(screen, (0, 104, 0), (780, 10, 100, 100), border_radius=20)
h2 = pygame.draw.rect(screen, (0, 104, 0), (780, 120, 100, 100), border_radius=20)
h3 = pygame.draw.rect(screen, (0, 104, 0), (780, 230, 100, 100), border_radius=20)
h4 = pygame.draw.rect(screen, (0, 104, 0), (780, 340, 100, 100), border_radius=20)
h5 = pygame.draw.rect(screen, (0, 104, 0), (780, 450, 100, 100), border_radius=20)
h6 = pygame.draw.rect(screen, (0, 104, 0), (780, 560, 100, 100), border_radius=20)
h7 = pygame.draw.rect(screen, (0, 104, 0), (780, 670, 100, 100), border_radius=20)
h8 = pygame.draw.rect(screen, (0, 104, 0), (780, 780, 100, 100), border_radius=20)
cercle = pygame.draw.circle(screen,(255, 255, 255), d4.center, 45)
cercle_2 = pygame.draw.circle(screen,(0, 0, 0), e4.center, 45)
cercle_3 = pygame.draw.circle(screen,(0, 0, 0), d5.center, 45)
cercle_4 = pygame.draw.circle(screen,(255, 255, 255), e5.center, 45)

cases = [a1, b1, c1, d1, e1, f1, g1, h1,
         a2, b2, c2, d2, e2, f2, g2, h2,
         a3, b3, c3, d3, e3, f3, g3, h3,
         a4, b4, c4, d4, e4, f4, g4, h4,
         a5, b5, c5, d5, e5, f5, g5, h5,
         a6, b6, c6, d6, e6, f6, g6, h6,
         a7, b7, c7, d7, e7, f7, g7, h7,
         a8, b8, c8, d8, e8, f8, g8, h8]

# AFFICHAGE DES ÉLÉMENTS :

pygame.display.update()


# BOUCLE RUNNING :

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            for i in cases:
                if i.collidepoint(pos):
                    if color_circle == (255, 255, 255):
                        pygame.draw.circle(screen, color_circle, i.center, 45)
                        color_circle = (0, 0, 0)
                    elif color_circle == (0, 0, 0):
                        pygame.draw.circle(screen, color_circle, i.center, 45)
                        color_circle = (255, 255, 255)
                    print(f"Position du clic : {pos}\nCase activée : {i}\n")

            pygame.display.update()

        if event.type == pygame.QUIT:
            running = False

pygame.quit()
