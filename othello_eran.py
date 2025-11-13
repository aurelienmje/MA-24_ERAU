# Version de l'othello d'Eran

import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Jeu de base")
clock = pygame.time.Clock()

ROUGE = (255, 0, 0)
NOIR = (0, 0, 0)
x, y = 400, 300

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 5
    if keys[pygame.K_RIGHT]:
        x += 5

    screen.fill(NOIR)
    pygame.draw.circle(screen, ROUGE, (x, y), 30)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
