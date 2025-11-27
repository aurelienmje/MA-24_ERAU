# PROMPTS ChatGPT :
# "copie juste ce code pour le faire pour a1 jusqu'à h8. (a1, a2, a3, a4, a5, a6 ,a7, a8, b1, b2, b3, b4....) :
# elif updater[2] == "a1":
#     a1 = updater"

import pygame

# DÉFINITION DES VARIABLES :

color_circle = (0, 0, 0)
cpt = 60

# PRÉPARATION DE PYGAME ET DE LA FENÊTRE

pygame.init()

screen = pygame.display.set_mode((890,890))
screen.fill((0,128,0))

pygame.display.set_caption("MA-24 : Bases de pygame")


# DÉFINITION DES CASES :

a1 = [pygame.draw.rect(screen, (0, 104, 0), (10, 10, 100, 100), border_radius=20), 0, "a1"]
a2 = [pygame.draw.rect(screen, (0, 104, 0), (10, 120, 100, 100), border_radius=20), 0, "a2"]
a3 = [pygame.draw.rect(screen, (0, 104, 0), (10, 230, 100, 100), border_radius=20), 0, "a3"]
a4 = [pygame.draw.rect(screen, (0, 104, 0), (10, 340, 100, 100), border_radius=20), 0, "a4"]
a5 = [pygame.draw.rect(screen, (0, 104, 0), (10, 450, 100, 100), border_radius=20), 0, "a5"]
a6 = [pygame.draw.rect(screen, (0, 104, 0), (10, 560, 100, 100), border_radius=20), 0, "a6"]
a7 = [pygame.draw.rect(screen, (0, 104, 0), (10, 670, 100, 100), border_radius=20), 0, "a7"]
a8 = [pygame.draw.rect(screen, (0, 104, 0), (10, 780, 100, 100), border_radius=20), 0, "a8"]
b1 = [pygame.draw.rect(screen, (0, 104, 0), (120, 10, 100, 100), border_radius=20), 0, "b1"]
b2 = [pygame.draw.rect(screen, (0, 104, 0), (120, 120, 100, 100), border_radius=20), 0, "b2"]
b3 = [pygame.draw.rect(screen, (0, 104, 0), (120, 230, 100, 100), border_radius=20), 0, "b3"]
b4 = [pygame.draw.rect(screen, (0, 104, 0), (120, 340, 100, 100), border_radius=20), 0, "b4"]
b5 = [pygame.draw.rect(screen, (0, 104, 0), (120, 450, 100, 100), border_radius=20), 0, "b5"]
b6 = [pygame.draw.rect(screen, (0, 104, 0), (120, 560, 100, 100), border_radius=20), 0, "b6"]
b7 = [pygame.draw.rect(screen, (0, 104, 0), (120, 670, 100, 100), border_radius=20), 0, "b7"]
b8 = [pygame.draw.rect(screen, (0, 104, 0), (120, 780, 100, 100), border_radius=20), 0, "b8"]
c1 = [pygame.draw.rect(screen, (0, 104, 0), (230, 10, 100, 100), border_radius=20), 0, "c1"]
c2 = [pygame.draw.rect(screen, (0, 104, 0), (230, 120, 100, 100), border_radius=20), 0, "c2"]
c3 = [pygame.draw.rect(screen, (0, 104, 0), (230, 230, 100, 100), border_radius=20), 0, "c3"]
c4 = [pygame.draw.rect(screen, (0, 104, 0), (230, 340, 100, 100), border_radius=20), 0, "c4"]
c5 = [pygame.draw.rect(screen, (0, 104, 0), (230, 450, 100, 100), border_radius=20), 0, "c5"]
c6 = [pygame.draw.rect(screen, (0, 104, 0), (230, 560, 100, 100), border_radius=20), 0, "c6"]
c7 = [pygame.draw.rect(screen, (0, 104, 0), (230, 670, 100, 100), border_radius=20), 0, "c7"]
c8 = [pygame.draw.rect(screen, (0, 104, 0), (230, 780, 100, 100), border_radius=20), 0, "c8"]
d1 = [pygame.draw.rect(screen, (0, 104, 0), (340, 10, 100, 100), border_radius=20), 0, "d1"]
d2 = [pygame.draw.rect(screen, (0, 104, 0), (340, 120, 100, 100), border_radius=20), 0, "d2"]
d3 = [pygame.draw.rect(screen, (0, 104, 0), (340, 230, 100, 100), border_radius=20), 0, "d3"]
d4 = [pygame.draw.rect(screen, (0, 104, 0), (340, 340, 100, 100), border_radius=20), 1, "d4"]
d5 = [pygame.draw.rect(screen, (0, 104, 0), (340, 450, 100, 100), border_radius=20), 2, "d5"]
d6 = [pygame.draw.rect(screen, (0, 104, 0), (340, 560, 100, 100), border_radius=20), 0, "d6"]
d7 = [pygame.draw.rect(screen, (0, 104, 0), (340, 670, 100, 100), border_radius=20), 0, "d7"]
d8 = [pygame.draw.rect(screen, (0, 104, 0), (340, 780, 100, 100), border_radius=20), 0, "d8"]
e1 = [pygame.draw.rect(screen, (0, 104, 0), (450, 10, 100, 100), border_radius=20), 0, "e1"]
e2 = [pygame.draw.rect(screen, (0, 104, 0), (450, 120, 100, 100), border_radius=20), 0, "e2"]
e3 = [pygame.draw.rect(screen, (0, 104, 0), (450, 230, 100, 100), border_radius=20), 0, "e3"]
e4 = [pygame.draw.rect(screen, (0, 104, 0), (450, 340, 100, 100), border_radius=20), 2, "e4"]
e5 = [pygame.draw.rect(screen, (0, 104, 0), (450, 450, 100, 100), border_radius=20), 1, "e5"]
e6 = [pygame.draw.rect(screen, (0, 104, 0), (450, 560, 100, 100), border_radius=20), 0, "e6"]
e7 = [pygame.draw.rect(screen, (0, 104, 0), (450, 670, 100, 100), border_radius=20), 0, "e7"]
e8 = [pygame.draw.rect(screen, (0, 104, 0), (450, 780, 100, 100), border_radius=20), 0, "e8"]
f1 = [pygame.draw.rect(screen, (0, 104, 0), (560, 10, 100, 100), border_radius=20), 0, "f1"]
f2 = [pygame.draw.rect(screen, (0, 104, 0), (560, 120, 100, 100), border_radius=20), 0, "f2"]
f3 = [pygame.draw.rect(screen, (0, 104, 0), (560, 230, 100, 100), border_radius=20), 0, "f3"]
f4 = [pygame.draw.rect(screen, (0, 104, 0), (560, 340, 100, 100), border_radius=20), 0, "f4"]
f5 = [pygame.draw.rect(screen, (0, 104, 0), (560, 450, 100, 100), border_radius=20), 0, "f5"]
f6 = [pygame.draw.rect(screen, (0, 104, 0), (560, 560, 100, 100), border_radius=20), 0, "f6"]
f7 = [pygame.draw.rect(screen, (0, 104, 0), (560, 670, 100, 100), border_radius=20), 0, "f7"]
f8 = [pygame.draw.rect(screen, (0, 104, 0), (560, 780, 100, 100), border_radius=20), 0, "f8"]
g1 = [pygame.draw.rect(screen, (0, 104, 0), (670, 10, 100, 100), border_radius=20), 0, "g1"]
g2 = [pygame.draw.rect(screen, (0, 104, 0), (670, 120, 100, 100), border_radius=20), 0, "g2"]
g3 = [pygame.draw.rect(screen, (0, 104, 0), (670, 230, 100, 100), border_radius=20), 0, "g3"]
g4 = [pygame.draw.rect(screen, (0, 104, 0), (670, 340, 100, 100), border_radius=20), 0, "g4"]
g5 = [pygame.draw.rect(screen, (0, 104, 0), (670, 450, 100, 100), border_radius=20), 0, "g5"]
g6 = [pygame.draw.rect(screen, (0, 104, 0), (670, 560, 100, 100), border_radius=20), 0, "g6"]
g7 = [pygame.draw.rect(screen, (0, 104, 0), (670, 670, 100, 100), border_radius=20), 0, "g7"]
g8 = [pygame.draw.rect(screen, (0, 104, 0), (670, 780, 100, 100), border_radius=20), 0, "g8"]
h1 = [pygame.draw.rect(screen, (0, 104, 0), (780, 10, 100, 100), border_radius=20), 0, "h1"]
h2 = [pygame.draw.rect(screen, (0, 104, 0), (780, 120, 100, 100), border_radius=20), 0, "h2"]
h3 = [pygame.draw.rect(screen, (0, 104, 0), (780, 230, 100, 100), border_radius=20), 0, "h3"]
h4 = [pygame.draw.rect(screen, (0, 104, 0), (780, 340, 100, 100), border_radius=20), 0, "h4"]
h5 = [pygame.draw.rect(screen, (0, 104, 0), (780, 450, 100, 100), border_radius=20), 0, "h5"]
h6 = [pygame.draw.rect(screen, (0, 104, 0), (780, 560, 100, 100), border_radius=20), 0, "h6"]
h7 = [pygame.draw.rect(screen, (0, 104, 0), (780, 670, 100, 100), border_radius=20), 0, "h7"]
h8 = [pygame.draw.rect(screen, (0, 104, 0), (780, 780, 100, 100), border_radius=20), 0, "h8"]


cases = [a1, b1, c1, d1, e1, f1, g1, h1,
         a2, b2, c2, d2, e2, f2, g2, h2,
         a3, b3, c3, d3, e3, f3, g3, h3,
         a4, b4, c4, d4, e4, f4, g4, h4,
         a5, b5, c5, d5, e5, f5, g5, h5,
         a6, b6, c6, d6, e6, f6, g6, h6,
         a7, b7, c7, d7, e7, f7, g7, h7,
         a8, b8, c8, d8, e8, f8, g8, h8]

for valeur in cases:
    if valeur[1] == 1:
        pygame.draw.circle(screen, (255, 255, 255), valeur[0].center, 45)
    elif valeur[1] == 2:
        pygame.draw.circle(screen, (0, 0, 0), valeur[0].center, 45)

# AFFICHAGE DES ÉLÉMENTS :

pygame.display.update()

# MAJ MEMOIRE CASES

def Update_Memory(updater):
    global cases, a1, b1, c1, d1, e1, f1, g1, h1, a2, b2, c2, d2, e2, f2, g2, h2, a3, b3, c3, d3, e3, f3, g3, h3, a4, b4, c4, d4, e4, f4, g4, h4, a5, b5, c5, d5, e5, f5, g5, h5, a6, b6, c6, d6, e6, f6, g6, h6, a7, b7, c7, d7, e7, f7, g7, h7, a8, b8, c8, d8, e8, f8, g8, h8
    if updater[2] == "a1":
        a1 = updater
    elif updater[2] == "a2":
        a2 = updater
    elif updater[2] == "a3":
        a3 = updater
    elif updater[2] == "a4":
        a4 = updater
    elif updater[2] == "a5":
        a5 = updater
    elif updater[2] == "a6":
        a6 = updater
    elif updater[2] == "a7":
        a7 = updater
    elif updater[2] == "a8":
        a8 = updater

    elif updater[2] == "b1":
        b1 = updater
    elif updater[2] == "b2":
        b2 = updater
    elif updater[2] == "b3":
        b3 = updater
    elif updater[2] == "b4":
        b4 = updater
    elif updater[2] == "b5":
        b5 = updater
    elif updater[2] == "b6":
        b6 = updater
    elif updater[2] == "b7":
        b7 = updater
    elif updater[2] == "b8":
        b8 = updater

    elif updater[2] == "c1":
        c1 = updater
    elif updater[2] == "c2":
        c2 = updater
    elif updater[2] == "c3":
        c3 = updater
    elif updater[2] == "c4":
        c4 = updater
    elif updater[2] == "c5":
        c5 = updater
    elif updater[2] == "c6":
        c6 = updater
    elif updater[2] == "c7":
        c7 = updater
    elif updater[2] == "c8":
        c8 = updater

    elif updater[2] == "d1":
        d1 = updater
    elif updater[2] == "d2":
        d2 = updater
    elif updater[2] == "d3":
        d3 = updater
    elif updater[2] == "d4":
        d4 = updater
    elif updater[2] == "d5":
        d5 = updater
    elif updater[2] == "d6":
        d6 = updater
    elif updater[2] == "d7":
        d7 = updater
    elif updater[2] == "d8":
        d8 = updater

    elif updater[2] == "e1":
        e1 = updater
    elif updater[2] == "e2":
        e2 = updater
    elif updater[2] == "e3":
        e3 = updater
    elif updater[2] == "e4":
        e4 = updater
    elif updater[2] == "e5":
        e5 = updater
    elif updater[2] == "e6":
        e6 = updater
    elif updater[2] == "e7":
        e7 = updater
    elif updater[2] == "e8":
        e8 = updater

    elif updater[2] == "f1":
        f1 = updater
    elif updater[2] == "f2":
        f2 = updater
    elif updater[2] == "f3":
        f3 = updater
    elif updater[2] == "f4":
        f4 = updater
    elif updater[2] == "f5":
        f5 = updater
    elif updater[2] == "f6":
        f6 = updater
    elif updater[2] == "f7":
        f7 = updater
    elif updater[2] == "f8":
        f8 = updater

    elif updater[2] == "g1":
        g1 = updater
    elif updater[2] == "g2":
        g2 = updater
    elif updater[2] == "g3":
        g3 = updater
    elif updater[2] == "g4":
        g4 = updater
    elif updater[2] == "g5":
        g5 = updater
    elif updater[2] == "g6":
        g6 = updater
    elif updater[2] == "g7":
        g7 = updater
    elif updater[2] == "g8":
        g8 = updater

    elif updater[2] == "h1":
        h1 = updater
    elif updater[2] == "h2":
        h2 = updater
    elif updater[2] == "h3":
        h3 = updater
    elif updater[2] == "h4":
        h4 = updater
    elif updater[2] == "h5":
        h5 = updater
    elif updater[2] == "h6":
        h6 = updater
    elif updater[2] == "h7":
        h7 = updater
    elif updater[2] == "h8":
        h8 = updater


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
                            i = i[0], 1, i[2]
                        elif color_circle == (0, 0, 0):
                            pygame.draw.circle(screen, color_circle, i[0].center, 45)
                            color_circle = (255, 255, 255)
                            i = i[0], 2, i[2]
                        print(f"Position du clic : {pos}\nCase activée : {i[2]}\n")
                        Update_Memory(i)
                        cases = [a1, b1, c1, d1, e1, f1, g1, h1,
                                 a2, b2, c2, d2, e2, f2, g2, h2,
                                 a3, b3, c3, d3, e3, f3, g3, h3,
                                 a4, b4, c4, d4, e4, f4, g4, h4,
                                 a5, b5, c5, d5, e5, f5, g5, h5,
                                 a6, b6, c6, d6, e6, f6, g6, h6,
                                 a7, b7, c7, d7, e7, f7, g7, h7,
                                 a8, b8, c8, d8, e8, f8, g8, h8]

                        print(f"""
                                 {a1[1]}, {b1[1]}, {c1[1]}, {d1[1]}, {e1[1]}, {f1[1]}, {g1[1]}, {h1[1]},
                                 {a2[1]}, {b2[1]}, {c2[1]}, {d2[1]}, {e2[1]}, {f2[1]}, {g2[1]}, {h2[1]},
                                 {a3[1]}, {b3[1]}, {c3[1]}, {d3[1]}, {e3[1]}, {f3[1]}, {g3[1]}, {h3[1]},
                                 {a4[1]}, {b4[1]}, {c4[1]}, {d4[1]}, {e4[1]}, {f4[1]}, {g4[1]}, {h4[1]},
                                 {a5[1]}, {b5[1]}, {c5[1]}, {d5[1]}, {e5[1]}, {f5[1]}, {g5[1]}, {h5[1]},
                                 {a6[1]}, {b6[1]}, {c6[1]}, {d6[1]}, {e6[1]}, {f6[1]}, {g6[1]}, {h6[1]},
                                 {a7[1]}, {b7[1]}, {c7[1]}, {d7[1]}, {e7[1]}, {f7[1]}, {g7[1]}, {h7[1]},
                                 {a8[1]}, {b8[1]}, {c8[1]}, {d8[1]}, {e8[1]}, {f8[1]}, {g8[1]}, {h8[1]}""")

                    if cpt == 0:
                        exit()

            pygame.display.update()

        if event.type == pygame.QUIT:
            running = False

pygame.quit()
