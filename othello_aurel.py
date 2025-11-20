import pygame
import sys

pygame.init()

# --- CONSTANTES ---
TAILLE_CASE = 80
NB_CASES = 8
LARGEUR = NB_CASES * TAILLE_CASE
HAUTEUR = NB_CASES * TAILLE_CASE

VERT_FOND = (0, 160, 0)
NOIR = (10, 10, 10)
BLANC = (240, 240, 240)
BLEU = (0, 120, 255)

# --- FENÊTRE ---
screen = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Othello / Reversi")

# --- TABLEAU DE JEU ---
# 0 = vide
# 1 = noir
# 2 = blanc
game = [[0] * 8 for _ in range(8)]

# position initiale
game[3][3] = 2
game[4][4] = 2
game[3][4] = 1
game[4][3] = 1

# Joueur actuel : 1 (noir) commence
current_player = 1

# Directions Othello
DIRS = [
    (-1, 0), (1, 0), (0, -1), (0, 1),
    (-1, -1), (-1, 1), (1, -1), (1, 1)
]
easter_egg_counter = 0
EASTER_EGG_TRIGGER = (3, 4)  # ligne, colonne du pion noir de départ

def show_easter_egg_popup():
    import tkinter as tk
    root = tk.Tk()
    root.title("Easter Egg !")

    label = tk.Label(root, text="j'ai utilisé mon code de l'année passée ", font=("Arial", 15))
    label.pack(padx=20, pady=20)

    close_btn = tk.Button(root, text="Fermer", command=root.destroy)
    close_btn.pack(pady=10)

    root.mainloop()


# --- FONCTION : coups valides ---
def get_valid_moves(player):
    opponent = 2 if player == 1 else 1
    valid = []

    for li in range(8):
        for col in range(8):
            if game[li][col] != 0:
                continue

            # Vérifier chaque direction
            for dl, dc in DIRS:
                l, c = li + dl, col + dc
                found_opponent = False

                # Tant qu'on voit l’adversaire
                while 0 <= l < 8 and 0 <= c < 8 and game[l][c] == opponent:
                    l += dl
                    c += dc
                    found_opponent = True

                # Trouvé adversaire + joueur derrière → coup valide
                if found_opponent and 0 <= l < 8 and 0 <= c < 8 and game[l][c] == player:
                    valid.append((li, col))
                    break

    return valid


# --- FONCTION : jouer un coup ---
def play_move(li, col, player):
    opponent = 2 if player == 1 else 1
    game[li][col] = player

    # Retourner les pions
    for dl, dc in DIRS:
        l, c = li + dl, col + dc
        path = []

        while 0 <= l < 8 and 0 <= c < 8 and game[l][c] == opponent:
            path.append((l, c))
            l += dl
            c += dc

        if path and 0 <= l < 8 and 0 <= c < 8 and game[l][c] == player:
            # Retourner
            for (rl, rc) in path:
                game[rl][rc] = player


# --- AFFICHAGE ---
def draw_board(valid_moves):
    screen.fill(VERT_FOND)

    # Cases
    for li in range(8):
        for col in range(8):
            pygame.draw.rect(screen, (0, 100, 0),
                             (col * TAILLE_CASE, li * TAILLE_CASE, TAILLE_CASE, TAILLE_CASE), 2)

            # Pions
            if game[li][col] == 1:
                pygame.draw.circle(screen, NOIR,
                                   (col * TAILLE_CASE + 40, li * TAILLE_CASE + 40), 30)
            elif game[li][col] == 2:
                pygame.draw.circle(screen, BLANC,
                                   (col * TAILLE_CASE + 40, li * TAILLE_CASE + 40), 30)

    # Coups valides : petits cercles bleus
    for (li, col) in valid_moves:
        pygame.draw.circle(screen, BLEU,
                           (col * TAILLE_CASE + 40, li * TAILLE_CASE + 40), 10)


# --- MAIN LOOP ---
clock = pygame.time.Clock()

while True:
    valid_moves = get_valid_moves(current_player)

    # Vérification du clic pour l'easter egg


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            col = x // TAILLE_CASE
            li = y // TAILLE_CASE

            # Vérification du clic pour l'easter egg
            if (li, col) == EASTER_EGG_TRIGGER:
                easter_egg_counter += 1

                if easter_egg_counter == 5:
                    show_easter_egg_popup()

            if (li, col) in valid_moves:
                play_move(li, col, current_player)
                current_player = 2 if current_player == 1 else 1

    draw_board(valid_moves)

    pygame.display.flip()
    clock.tick(60)
