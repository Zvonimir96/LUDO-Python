import pygame

import player
from buttonListener import ButtonListener
from dice import Dice
from enumerator.gameState import GameState
from map import Map
from player import Player

pygame.init()

running = True

screen = pygame.display.set_mode([1000, 1000])
Map.create()
Player.create()


def startGame():
    for player in Player.players:
        if not player.playable:
            player.setInactive()
        else:
            Player.onTurn = player


def nextPlayer():
    orderNumber = Player.onTurn.getOrderNumber() + 1

    if orderNumber >= len(Player.players):
        orderNumber = 0

    Player.onTurn = Player.players[orderNumber]

    global state
    state = GameState(orderNumber)

    if not Player.onTurn.isPlayable():
        nextPlayer()

count = 0

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
                startGame()
                nextPlayer()

            if event.key == pygame.K_2:
                Dice.roll(Player.onTurn.getColor())

            if event.key == pygame.K_3:
                nextPlayer()

            if event.key == pygame.K_4:
                print(count)

    screen.fill((0, 0, 0))
    Map.draw(screen)
    pygame.display.flip()

pygame.quit()
