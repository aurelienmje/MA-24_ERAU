import pygame

pygame.init()

screen = pygame.display.set_mode((890,890))

pygame.display.set_caption("MA-24 : Bases de pygame")

a = 10
b = 10

"""for y in range (0, 8):
    for i in range(0, 8):
            pygame.draw.rect(screen, (0, 104, 0), (b, a, 100, 100), 0)
            a = a + 110
            print(a, b)
    a = 10
    b = b + 110"""

a1 = pygame.draw.rect(screen, (0, 104, 0), (10, 10, 100, 100), 0)
a2 = pygame.draw.rect(screen, (0, 104, 0), (10, 120, 100, 100), 0)
a3 = pygame.draw.rect(screen, (0, 104, 0), (10, 230, 100, 100), 0)
a4 = pygame.draw.rect(screen, (0, 104, 0), (10, 340, 100, 100), 0)
a5 = pygame.draw.rect(screen, (0, 104, 0), (10, 450, 100, 100), 0)
a6 = pygame.draw.rect(screen, (0, 104, 0), (10, 560, 100, 100), 0)
a7 = pygame.draw.rect(screen, (0, 104, 0), (10, 670, 100, 100), 0)
a8 = pygame.draw.rect(screen, (0, 104, 0), (10, 780, 100, 100), 0)
b1 = pygame.draw.rect(screen, (0, 104, 0), (120, 10, 100, 100), 0)
b2 = pygame.draw.rect(screen, (0, 104, 0), (120, 120, 100, 100), 0)
b3 = pygame.draw.rect(screen, (0, 104, 0), (120, 230, 100, 100), 0)
b4 = pygame.draw.rect(screen, (0, 104, 0), (120, 340, 100, 100), 0)
b5 = pygame.draw.rect(screen, (0, 104, 0), (120, 450, 100, 100), 0)
b6 = pygame.draw.rect(screen, (0, 104, 0), (120, 560, 100, 100), 0)
b7 = pygame.draw.rect(screen, (0, 104, 0), (120, 670, 100, 100), 0)
b8 = pygame.draw.rect(screen, (0, 104, 0), (120, 780, 100, 100), 0)
c1 = pygame.draw.rect(screen, (0, 104, 0), (230, 10, 100, 100), 0)
c2 = pygame.draw.rect(screen, (0, 104, 0), (230, 120, 100, 100), 0)
c3 = pygame.draw.rect(screen, (0, 104, 0), (230, 230, 100, 100), 0)
c4 = pygame.draw.rect(screen, (0, 104, 0), (230, 340, 100, 100), 0)
c5 = pygame.draw.rect(screen, (0, 104, 0), (230, 450, 100, 100), 0)
c6 = pygame.draw.rect(screen, (0, 104, 0), (230, 560, 100, 100), 0)
c7 = pygame.draw.rect(screen, (0, 104, 0), (230, 670, 100, 100), 0)
c8 = pygame.draw.rect(screen, (0, 104, 0), (230, 780, 100, 100), 0)
d1 = pygame.draw.rect(screen, (0, 104, 0), (340, 10, 100, 100), 0)
d2 = pygame.draw.rect(screen, (0, 104, 0), (340, 120, 100, 100), 0)
d3 = pygame.draw.rect(screen, (0, 104, 0), (340, 230, 100, 100), 0)
d4 = pygame.draw.rect(screen, (0, 104, 0), (340, 340, 100, 100), 0)
d5 = pygame.draw.rect(screen, (0, 104, 0), (340, 450, 100, 100), 0)
d6 = pygame.draw.rect(screen, (0, 104, 0), (340, 560, 100, 100), 0)
d7 = pygame.draw.rect(screen, (0, 104, 0), (340, 670, 100, 100), 0)
d8 = pygame.draw.rect(screen, (0, 104, 0), (340, 780, 100, 100), 0)
e1 = pygame.draw.rect(screen, (0, 104, 0), (450, 10, 100, 100), 0)
e2 = pygame.draw.rect(screen, (0, 104, 0), (450, 120, 100, 100), 0)
e3 = pygame.draw.rect(screen, (0, 104, 0), (450, 230, 100, 100), 0)
e4 = pygame.draw.rect(screen, (0, 104, 0), (450, 340, 100, 100), 0)
e5 = pygame.draw.rect(screen, (0, 104, 0), (450, 450, 100, 100), 0)
e6 = pygame.draw.rect(screen, (0, 104, 0), (450, 560, 100, 100), 0)
e7 = pygame.draw.rect(screen, (0, 104, 0), (450, 670, 100, 100), 0)
e8 = pygame.draw.rect(screen, (0, 104, 0), (450, 780, 100, 100), 0)
f1 = pygame.draw.rect(screen, (0, 104, 0), (560, 10, 100, 100), 0)
f2 = pygame.draw.rect(screen, (0, 104, 0), (560, 120, 100, 100), 0)
f3 = pygame.draw.rect(screen, (0, 104, 0), (560, 230, 100, 100), 0)
f4 = pygame.draw.rect(screen, (0, 104, 0), (560, 340, 100, 100), 0)
f5 = pygame.draw.rect(screen, (0, 104, 0), (560, 450, 100, 100), 0)
f6 = pygame.draw.rect(screen, (0, 104, 0), (560, 560, 100, 100), 0)
f7 = pygame.draw.rect(screen, (0, 104, 0), (560, 670, 100, 100), 0)
f8 = pygame.draw.rect(screen, (0, 104, 0), (560, 780, 100, 100), 0)
g1 = pygame.draw.rect(screen, (0, 104, 0), (670, 10, 100, 100), 0)
g2 = pygame.draw.rect(screen, (0, 104, 0), (670, 120, 100, 100), 0)
g3 = pygame.draw.rect(screen, (0, 104, 0), (670, 230, 100, 100), 0)
g4 = pygame.draw.rect(screen, (0, 104, 0), (670, 340, 100, 100), 0)
g5 = pygame.draw.rect(screen, (0, 104, 0), (670, 450, 100, 100), 0)
g6 = pygame.draw.rect(screen, (0, 104, 0), (670, 560, 100, 100), 0)
g7 = pygame.draw.rect(screen, (0, 104, 0), (670, 670, 100, 100), 0)
g8 = pygame.draw.rect(screen, (0, 104, 0), (670, 780, 100, 100), 0)
h1 = pygame.draw.rect(screen, (0, 104, 0), (780, 10, 100, 100), 0)
h2 = pygame.draw.rect(screen, (0, 104, 0), (780, 120, 100, 100), 0)
h3 = pygame.draw.rect(screen, (0, 104, 0), (780, 230, 100, 100), 0)
h4 = pygame.draw.rect(screen, (0, 104, 0), (780, 340, 100, 100), 0)
h5 = pygame.draw.rect(screen, (0, 104, 0), (780, 450, 100, 100), 0)
h6 = pygame.draw.rect(screen, (0, 104, 0), (780, 560, 100, 100), 0)
h7 = pygame.draw.rect(screen, (0, 104, 0), (780, 670, 100, 100), 0)
h8 = pygame.draw.rect(screen, (0, 104, 0), (780, 780, 100, 100), 0)

pygame.display.flip()

def ()
#regarde le fichier txt
running = True
while running:
    """for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        btn_presse = pygame.key.get_pressed()
        if btn_presse[pygame.K_RIGHT]:
            bouge_droite()
        elif btn_presse[pygame.K_LEFT]:
            bouge_gauche()
        elif btn_presse[pygame.K_q]:
            running = False
        pygame.display.update()"""

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            print(pos)
            a,b = pos
            pygame.draw.circle(screen, (255, 255, 255), (a, b), 50)
            for i,  in enumerate(cases):
                if i.collidepoint(event.pos):
                    pygame.draw.circle(screen, (255, 255, 255), (a, b), 50)

            pygame.display.update()

        if event.type == pygame.QUIT:
            running = False

pygame.quit()