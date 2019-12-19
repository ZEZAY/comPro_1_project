import pygame
from PS import *


def main():
    SQUARESZE_COLS = 100
    SQUARESZE_ROW = 153

    NUM_COLS = 5
    NUM_ROW = 3

    WIDTH = NUM_COLS * SQUARESZE_COLS
    HEIGHT = NUM_ROW * SQUARESZE_ROW

    pygame.init()
    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    pygame.display.set_caption('PAIRS GAME')
    board = PS()

    running = True
    while running:
        screen.fill((0, 0, 0))
        board.draw(screen)
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] and not board.get_game_over():
                    pos = pygame.mouse.get_pos()
                    x, y = (pos[0] // 100), (pos[1] // 153)
                    board.get_mouse(x, y)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and board.get_game_over():
                    board.reset()
                if event.key == pygame.K_ESCAPE:
                    running = False

        board.set_game_over()

    return int(board.get_score())
