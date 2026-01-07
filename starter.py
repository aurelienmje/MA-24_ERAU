import pygame
import menu
from menu import *
from tkinter.messagebox import *
import gfx

# logique : joueur courant 1 = noir, -1 = blanc. On commence noir.
player = 1
easter_clicks = 0  # compteur pour l'easter egg

def easter_egg():
    showinfo(
        title="🎉 Easter Egg 🎉",
        message=
"""Ce jeu a été codé par :

Aurélien
Eran
et avec l'aide de ChatGPT 😄

   (•‿•)
  <)   )╯
   /   \\

Bravo, tu as trouvé le secret !
"""
    )
def coord_from_rect(rect):
    # find board coordinates stored in rect entry
    for entry in gfx.cases:
        if entry[0] == rect:
            return entry[2]
    return None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = event.pos
            # Coin haut-droite : zone de 100x100 pixels en haut à droite du plateau
            if pos[0] >= gfx.screen.get_width() - 110 and pos[0] <= gfx.screen.get_width() - 10 and pos[1] >= 10 and \
                    pos[1] <= 110:
                easter_clicks += 1
                if easter_clicks == 6:
                    easter_egg()
                    easter_clicks = 0
            else:
                easter_clicks = 0
            clicked_rect = None
            for entry in gfx.cases:
                if entry[0].collidepoint(pos):
                    clicked_rect = entry[0]
                    break
            if clicked_rect is None:
                continue
            rc = coord_from_rect(clicked_rect)
            if rc is None:
                continue
            r,c = rc

            valid, flips = gfx.is_valid_move(gfx.board, player, r, c)

            if not valid:
                print("Coup invalide")
            else:
                gfx.apply_move(gfx.board, player, r, c)
                # redraw board
                gfx.screen.fill((0,128,0))
                gfx.cases = gfx.dessiner_cases(gfx.board)
                # changer de joueur ou gérer passe
                opponent = -player
                if gfx.legal_moves(gfx.board, opponent):
                    player = opponent
                else:
                    if not gfx.legal_moves(gfx.board, player):
                        # aucun coup pour les deux -> fin
                        black = sum(1 for row in gfx.board for v in row if v == 1)
                        white = sum(1 for row in gfx.board for v in row if v == -1)
                        if black > white:
                            showinfo(title="Fin du jeu", message=f"Les Noirs gagnent {black} à {white}")
                        elif white > black:
                            showinfo(title="Fin du jeu", message=f"Les Blancs gagnent {white} à {black}")
                        else:
                            showinfo(title="Fin du jeu", message=f"Égalité {black} à {white}")
                        gfx.board = gfx.initial_board()
                        gfx.screen.fill((0,128,0))
                        gfx.cases = gfx.dessiner_cases(gfx.board)
                        player = 1
                # dessiner surbrillance des coups possibles pour player courant
                highs = gfx.highlight_moves(gfx.board, player)
                for rect in highs:
                    pygame.draw.rect(gfx.screen, (200, 200, 80), rect, width=4, border_radius=20)
                pygame.display.update()

        if event.type == pygame.QUIT:
            running = False

pygame.quit()
