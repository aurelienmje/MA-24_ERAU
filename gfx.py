import pygame

# DÉFINITION DES VARIABLES :
color_circle = (0, 0, 0)  # joueur courant: noir=(0,0,0) affichage, mais logique utilise 1 = noir, -1 = blanc

# PRÉPARATION DE PYGAME ET DE LA FENÊTRE
pygame.init()
screen = pygame.display.set_mode((890,890))
screen.fill((0,128,0))
pygame.display.set_caption("MA-24 : Bases de pygame")

# Logique Othello : représentation 8x8 with values 0 empty, 1 black, -1 white
BOARD_SIZE = 8
directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

def in_bounds(r,c):
    return 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE

def make_empty_board():
    return [[0 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def initial_board():
    b = make_empty_board()
    mid = BOARD_SIZE // 2
    # standard initial position: (3,3)=white(-1),(3,4)=black(1),(4,3)=black(1),(4,4)=white(-1)
    b[mid-1][mid-1] = -1
    b[mid-1][mid]   = 1
    b[mid][mid-1]   = 1
    b[mid][mid]     = -1
    return b

def is_valid_move(board, player, r, c):
    if not in_bounds(r,c) or board[r][c] != 0:
        return False, []
    captured = []
    for dr,dc in directions:
        i, j = r+dr, c+dc
        temp = []
        if not in_bounds(i,j) or board[i][j] != -player:
            continue
        temp.append((i,j))
        while True:
            i += dr; j += dc
            if not in_bounds(i,j):
                temp = []
                break
            if board[i][j] == 0:
                temp = []
                break
            if board[i][j] == player:
                break
            temp.append((i,j))
        if temp and in_bounds(i,j) and board[i][j] == player:
            captured.extend(temp)
    return (len(captured) > 0), captured

def legal_moves(board, player):
    moves = []
    for r in range(BOARD_SIZE):
        for c in range(BOARD_SIZE):
            valid, _ = is_valid_move(board, player, r, c)
            if valid:
                moves.append((r,c))
    return moves

def highlight_moves(board, player):
    # renvoie une liste de rects à surligner
    highlights = []
    for entry in cases:
        r,c = entry[2]
        valid, _ = is_valid_move(board, player, r, c)
        if valid:
            highlights.append(entry[0])
    return highlights

def apply_move(board, player, r, c):
    valid, to_flip = is_valid_move(board, player, r, c)
    if not valid:
        raise ValueError("Invalid move")
    board[r][c] = player
    for i,j in to_flip:
        board[i][j] = player

# Dessin : cases list stores [rect, value] where value 0 empty, 1 white, 2 black for rendering legacy
def dessiner_cases(board):
    compteur = 0
    posx = 10
    cases = []
    for row in range(8):
        posy = 10
        for col in range(8):
            rect = pygame.draw.rect(screen, (0, 104, 0), (posx, posy, 100, 100), border_radius=20)
            # map logical board to rendering values: 0 -> 0, 1 -> 2 (black), -1 -> 1 (white)
            cell = board[row][col]
            if cell == -1:
                val = 1
            elif cell == 1:
                val = 2
            else:
                val = 0
            cases.append([rect, val, (row, col)])
            posy += 110
            compteur += 1
        posx += 110

    for cercle in cases:
        if cercle[1] == 1:
            pygame.draw.circle(screen, (255, 255, 255), cercle[0].center, 45)
        elif cercle[1] == 2:
            pygame.draw.circle(screen, (0, 0, 0), cercle[0].center, 45)

    pygame.display.update()
    return cases

# Variables exportées pour Starter.py
board = initial_board()
cases = dessiner_cases(board)
