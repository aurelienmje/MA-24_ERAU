# Version de l'othello d'Aurélien
import pygame
import sys

pygame.init()

# --- CONSTANTES ---
TAILLE_CASE = 50
NB_CASES = 8
LARGEUR = NB_CASES * TAILLE_CASE
HAUTEUR = NB_CASES * TAILLE_CASE

BLANC = (255, 255, 255)
VERT = (0, 180, 0)

# --- FENÊTRE ---
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("plateau de jeu othello")

# --- TABLEAU DE JEU (8x8) ---
game = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

# Case sélectionnée (li, col) ou (-1, -1)
selected = (-1, -1)



def draw_board():
    for li in range(8):
        for col in range(8):
            # Plateau vert
            pygame.draw.rect(screen, (0, 255, 0),
                             (col * TAILLE_CASE, li * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE))

            # Case sélectionnée entourée en vert
            if (li, col) == selected:
                pygame.draw.rect(screen, (255, 0, 0),
                                 (col * TAILLE_CASE, li * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE), 5)


# --- CALCUL LI, COL DEPUIS UN CLIC ---
def get_case_from_mouse(pos):
    x, y = pos
    col = x // TAILLE_CASE
    li = y // TAILLE_CASE

    if 0 <= li < 8 and 0 <= col < 8:
        return li, col
    return None


# --- BOUCLE PRINCIPALE ---
clock = pygame.time.Clock()

while True:
      # fond vert foncé

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # clic souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            case = get_case_from_mouse(event.pos)
            if case:
                li, col = case
                print("Clic sur :", li, col)

                # sélectionner / désélectionner
                if selected == (li, col):
                    selected = (-1, -1)
                else:
                    selected = (li, col)


    draw_board()

    pygame.display.flip()
    clock.tick(60)
