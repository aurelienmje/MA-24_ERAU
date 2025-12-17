import pygame
import sys

pygame.init()


WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("menu OOHTLEO")

# Couleurs
WHITE = (0, 205, 10)
BLACK = (0, 0, 0)
GRAY = (255, 250, 250)
BLUE = (22, 0, 205)


font = pygame.font.Font(None, 50)
button_font = pygame.font.Font(None, 36)


play_button = pygame.Rect(200, 150, 200, 50)
quit_button = pygame.Rect(200, 230, 200, 50)

def draw_menu():
    screen.fill(WHITE)


    title = font.render("MENU OOTHLEO", True, BLACK)
    screen.blit(title, (WIDTH//2 - title.get_width()//2, 50))


    pygame.draw.rect(screen, BLUE, play_button)
    pygame.draw.rect(screen, GRAY, quit_button)


    play_text = button_font.render("Jouer", True, WHITE)
    quit_text = button_font.render("Quitter", True, WHITE)

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