import pygame

from buttonListener import ButtonListener
from dice import Dice
from map import Map
from player import Player
from enumerator.gameState import gameState, gameEnumerator

pygame.init()

running = True

screen = pygame.display.set_mode([1000, 1000])

Map.create()
Player.create()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            ButtonListener.buttonAction(pygame.mouse.get_pos())

        if event.type == pygame.KEYDOWN:
            """
            if event.key == pygame.K_1:
                Path.changeModes()
            if event.key == pygame.K_2:
                House.changeModes()
            if event.key == pygame.K_3:
                SafeHouse.changeModes()
            if event.key == pygame.K_4:
                Button.changeImages()
            """
            if event.key == pygame.K_1:
                Player.startGame()
                gameState = gameEnumerator[1]
                print(gameState)

    screen.fill((0, 0, 0))
    Map.draw(screen)
    pygame.display.flip()

pygame.quit()
