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
    width = 420
    height = 420
    cellAmount = 21

    screen = pygame.display.set_mode((width, height))
    running = True
    map = ZeroField(cellAmount)

    map[15][15] = 1

    map[5][5] = 1
    while running:
        pygame.display.flip()
        print(map)
        for y in range(cellAmount):
             for x in range(cellAmount):
                if(map[x][y] == 0):
                    pygame.draw.rect(screen, (0, 0, 0), (x * cellAmount - 1, y * cellAmount - 1, 20, 20))
                else:
                    tup = 255 - 10 * map[x][y]
                    pygame.draw.rect(screen, (tup, tup, tup), (x * cellAmount - 1, y * cellAmount - 1, 20, 20))

        for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    running = False
                if events.type == pygame.KEYDOWN:
                     if events.key == pygame.K_SPACE:
                          ExpandSpill(map)


main()