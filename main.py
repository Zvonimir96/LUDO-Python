import pygame
import time

from mapElements.buttons.buttonListener import ButtonListener
from mapElements.dice import Dice
from map import Map
from mapElements.buttons.button import Button
from mapElements.field import Field
from player import Player
from settings import fadeTime

pygame.init()

clock = time.time() + fadeTime
running = True

screen = pygame.display.set_mode([1000, 1000])
Map.create()
Player.create()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            ButtonListener.buttonClicked(Button.isAnyButtonClicked(pygame.mouse.get_pos()))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_2:
                pass

    if clock <= time.time():
        clock = time.time() + fadeTime
        Field.fadeAll()
        Button.fadeAll()
        Dice.doRainbow()

    Dice.doAnimation()

    screen.fill((0, 0, 0))
    Map.draw(screen)
    pygame.display.flip()

pygame.quit()
