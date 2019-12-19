import pygame
from RL import *
import random


def main():
    SQUARESZE_COLS = 100
    SQUARESZE_ROW = 100
    NUM_COLS = 15
    NUM_ROW = 7
    WIDTH = NUM_COLS * SQUARESZE_COLS
    HEIGHT = NUM_ROW * SQUARESZE_ROW

    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('ROULETTE GAME')
    board = RL()

    running = True
    while running:
        screen.fill((0, 76, 0))
        board.draw(screen)
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and not board.get_game_over():
                    pos = pygame.mouse.get_pos()
                    x, y = int((pos[0] - (100 / 3)) // (100 / 3)), int((pos[1] - (50 - (100 / 3))) // (100 / 3))
                    board.get_mouse(x, y)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and board.get_game_over():
                    running = False

        board.set_game_over()
        board.set_time_over()
    return int(board.get_score())
