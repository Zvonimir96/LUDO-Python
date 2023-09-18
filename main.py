import pygame
from layot import draw
from utilities import display_width, display_height
from controller import init, is_button_clicked
from animaton import update as update_animations

pygame.init()
init()

screen = pygame.display.set_mode((display_width, display_height))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONUP:
            is_button_clicked(pygame.mouse.get_pos())

    screen.fill((0, 0, 0))

    update_animations()
    draw(screen)

    pygame.display.flip()

pygame.quit()
