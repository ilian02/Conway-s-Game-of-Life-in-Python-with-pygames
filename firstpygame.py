import pygame
import copy
import numpy as np
from time import sleep
import math

pygame.init()

WIDTH = 900
HEIGHT = 900

NODESIZE = 25;

screen = pygame.display.set_mode((WIDTH, HEIGHT))


WHITE=(255,255,255)
GREY=(150, 150, 150)

pygame.display.set_caption("Game of Life by Conway")


ARRAYSIZE = 35

def shouldItLive(row, col, table):
    neighbors = 0

    if 0 < row < ARRAYSIZE - 1:
        if 0 < col < ARRAYSIZE - 1:
            if table[row - 1][col - 1] == 1:
                neighbors += 1
            if table[row + 1][col + 1] == 1:
                neighbors += 1
            if table[row - 1][col + 1] == 1:
                neighbors += 1
            if table[row + 1][col - 1] == 1:
                neighbors += 1
            if table[row - 1][col] == 1:
                neighbors += 1
            if table[row + 1][col] == 1:
                neighbors += 1
            if table[row][col - 1] == 1:
                neighbors += 1
            if table[row][col + 1] == 1:
                neighbors += 1
        elif col == 0:
            if table[row - 1][ARRAYSIZE - 1] == 1:
                neighbors += 1
            if table[row + 1][col + 1] == 1:
                neighbors += 1
            if table[row - 1][col + 1] == 1:
                neighbors += 1
            if table[row + 1][ARRAYSIZE - 1] == 1:
                neighbors += 1
            if table[row - 1][col] == 1:
                neighbors += 1
            if table[row + 1][col] == 1:
                neighbors += 1
            if table[row][ARRAYSIZE - 1] == 1:
                neighbors += 1
            if table[row][col + 1] == 1:
                neighbors += 1
        elif col == ARRAYSIZE - 1:
            if table[row - 1][col - 1] == 1:
                neighbors += 1
            if table[row + 1][0] == 1:
                neighbors += 1
            if table[row - 1][0] == 1:
                neighbors += 1
            if table[row + 1][col - 1] == 1:
                neighbors += 1
            if table[row - 1][col] == 1:
                neighbors += 1
            if table[row + 1][col] == 1:
                neighbors += 1
            if table[row][col - 1] == 1:
                neighbors += 1
            if table[row][0] == 1:
                neighbors += 1
    elif row == 0:
        if 0 < col < ARRAYSIZE - 1:
            if table[ARRAYSIZE - 1][col - 1] == 1:
                neighbors += 1
            if table[row + 1][col + 1] == 1:
                neighbors += 1
            if table[ARRAYSIZE - 1][col + 1] == 1:
                neighbors += 1
            if table[row + 1][col - 1] == 1:
                neighbors += 1
            if table[ARRAYSIZE - 1][col] == 1:
                neighbors += 1
            if table[row + 1][col] == 1:
                neighbors += 1
            if table[row][col - 1] == 1:
                neighbors += 1
            if table[row][col + 1] == 1:
                neighbors += 1
        elif col == 0:
            if table[ARRAYSIZE - 1][ARRAYSIZE - 1] == 1:
                neighbors += 1
            if table[row + 1][col + 1] == 1:
                neighbors += 1
            if table[ARRAYSIZE - 1][col + 1] == 1:
                neighbors += 1
            if table[row + 1][ARRAYSIZE - 1] == 1:
                neighbors += 1
            if table[ARRAYSIZE - 1][col] == 1:
                neighbors += 1
            if table[row + 1][col] == 1:
                neighbors += 1
            if table[row][ARRAYSIZE - 1] == 1:
                neighbors += 1
            if table[row][col + 1] == 1:
                neighbors += 1
        elif col == ARRAYSIZE - 1:
            if table[ARRAYSIZE - 1][col - 1] == 1:
                neighbors += 1
            if table[row + 1][0] == 1:
                neighbors += 1
            if table[ARRAYSIZE - 1][0] == 1:
                neighbors += 1
            if table[row + 1][col - 1] == 1:
                neighbors += 1
            if table[ARRAYSIZE - 1][col] == 1:
                neighbors += 1
            if table[row + 1][col] == 1:
                neighbors += 1
            if table[row][col - 1] == 1:
                neighbors += 1
            if table[row][0] == 1:
                neighbors += 1
    elif row == ARRAYSIZE - 1:
        if 0 < col < ARRAYSIZE - 1:
            if table[row - 1][col - 1] == 1:
                neighbors += 1
            if table[0][col + 1] == 1:
                neighbors += 1
            if table[row - 1][col + 1] == 1:
                neighbors += 1
            if table[0][col - 1] == 1:
                neighbors += 1
            if table[row - 1][col] == 1:
                neighbors += 1
            if table[0][col] == 1:
                neighbors += 1
            if table[row][col - 1] == 1:
                neighbors += 1
            if table[row][col + 1] == 1:
                neighbors += 1
        elif col == 0:
            if table[row - 1][ARRAYSIZE - 1] == 1:
                neighbors += 1
            if table[0][col + 1] == 1:
                neighbors += 1
            if table[row - 1][col + 1] == 1:
                neighbors += 1
            if table[0][ARRAYSIZE - 1] == 1:
                neighbors += 1
            if table[row - 1][col] == 1:
                neighbors += 1
            if table[0][col] == 1:
                neighbors += 1
            if table[row][ARRAYSIZE - 1] == 1:
                neighbors += 1
            if table[row][col + 1] == 1:
                neighbors += 1
        elif col == ARRAYSIZE - 1:
            if table[row - 1][col - 1] == 1:
                neighbors += 1
            if table[0][0] == 1:
                neighbors += 1
            if table[row - 1][0] == 1:
                neighbors += 1
            if table[0][col - 1] == 1:
                neighbors += 1
            if table[row - 1][col] == 1:
                neighbors += 1
            if table[0][col] == 1:
                neighbors += 1
            if table[row][col - 1] == 1:
                neighbors += 1
            if table[row][0] == 1:
                neighbors += 1


    if (neighbors == 3 or neighbors == 2) and table[row][col] == 1:
        return True
    elif neighbors == 3 and table[row][col] == 0:
        return True
    else:
        return False


def do_magic(table):
    newTable = copy.deepcopy(table)

    for row in range(0, ARRAYSIZE):
        for col in range(0, ARRAYSIZE):
            if shouldItLive(row, col, table):
                newTable[row][col] = 1
            else:
                newTable[row][col] = 0
    return newTable


board = np.zeros(ARRAYSIZE*ARRAYSIZE).reshape(ARRAYSIZE, ARRAYSIZE)

onHold = True
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            onHold = not onHold
        if event.type == pygame.MOUSEBUTTONUP and onHold == True:
            x, y = pygame.mouse.get_pos()
            if board[math.ceil(x / NODESIZE) - 1][math.ceil(y / NODESIZE) - 1] == 1:
                board[math.ceil(x / NODESIZE) - 1][math.ceil(y / NODESIZE) - 1] = 0
            else:
                board[math.ceil(x / NODESIZE) - 1][math.ceil(y / NODESIZE) - 1] = 1

    for x in range(0, ARRAYSIZE):
        for y in range(0, ARRAYSIZE):
            if board[x][y] == 1:
                pygame.draw.rect(screen, WHITE, (x*NODESIZE, y*NODESIZE, NODESIZE - 1, NODESIZE - 1))
            else:
                pygame.draw.rect(screen, GREY, (x*NODESIZE, y*NODESIZE, NODESIZE - 1, NODESIZE - 1))

    if not onHold:
        board = do_magic(board)
        sleep(0.1)

    pygame.display.update()
