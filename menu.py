import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("menu othello")

# Couleurs
GREEN = (28, 199, 28)
BLACK = (0, 0, 0)
GRAY = (38, 240, 219)
BLUE = (42, 94, 86)


font = pygame.font.Font(None, 70)
button_font = pygame.font.Font(None, 36)


play_button = pygame.Rect(200, 150, 200, 50)
quit_button = pygame.Rect(200, 230, 200, 50)

def draw_menu():
    screen.fill(GREEN)


    title = font.render("¦__ERAU-GAME__¦", True, BLACK)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))


    pygame.draw.rect(screen, BLUE, play_button)
    pygame.draw.rect(screen, GRAY, quit_button)


    play_text = button_font.render("JOUER", True, GREEN)
    quit_text = button_font.render("QUITTER", True, GREEN)

    screen.blit(play_text, (play_button.centerx - play_text.get_width()//2,
                             play_button.centery - play_text.get_height()//2))
    screen.blit(quit_text, (quit_button.centerx - quit_text.get_width()//2,
                             quit_button.centery - quit_text.get_height()//2))

    pygame.display.flip()


running = True
while running:
    draw_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:

            if quit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()