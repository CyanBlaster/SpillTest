import sys
import pygame
import datetime
import math
import pygame.freetype
import random

pygame.init()


def ZeroField(n):
    return [[0] * n for i in range(n)]

def findMax(map):
    max = 1
    for y in range(0, len(map)):
        for x in range(0, len(map[y])):      
             if(map[x][y] > max):
                  max = map[x][y]
    return max



def ExpandSpill(map):
    a = findMax(map)
    for y in range(0, len(map)):
         for x in range(0, len(map[y])):      
                if(map[x][y] == a):
                    if(y < len(map) - 1 and map[x][y + 1] == 0):
                        map[x][y + 1] = a + 1
                    if(y > 0 and map[x][y - 1] == 0):
                        map[x][y - 1] = a + 1
                    if(x > 0 and map[x - 1][y] == 0):
                        map[x - 1][y] = a + 1
                    if(x < len(map[y]) - 1 and map[x + 1][y] == 0):
                        map[x + 1][y] = a + 1
                
def main():
    width = 800
    height = 800
    cellAmount = 40
    cellHeight = height/cellAmount
    cellWidth = width/cellAmount

    screen = pygame.display.set_mode((width, height))
    running = True
    map = ZeroField(cellAmount)

    map[5][30] = 1

    map[30][22] = -1
    map[30][23] = -1
    map[30][24] = -1
    map[30][25] = -1
    map[30][26] = -1
    map[30][27] = -1
    map[30][28] = -1
    map[30][29] = -1
    map[30][30] = -1
    map[30][31] = -1
    map[30][32] = -1
    map[30][33] = -1
    map[30][34] = -1
    map[30][35] = -1
    map[30][36] = -1
    map[30][37] = -1

    while running:
        pygame.display.flip()
        print(map)
        for y in range(len(map)):
             for x in range(len(map[y])):
                if(map[x][y] == 0):
                    pygame.draw.rect(screen, (0, 0, 0), (x * cellHeight - 1, y * cellWidth - 1, cellHeight, cellWidth))
                elif(map[x][y] == -1):
                    pygame.draw.rect(screen, (200, 100, 1), (x * cellHeight - 1, y * cellWidth - 1, cellHeight, cellWidth))
                else:
                    tup = 255 - 5 * map[x][y]
                    pygame.draw.rect(screen, (tup, tup, tup), (x * cellHeight - 1, y * cellWidth - 1, cellHeight, cellWidth))

        for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    running = False
                if events.type == pygame.KEYDOWN:
                     if events.key == pygame.K_SPACE:
                          ExpandSpill(map)


main()