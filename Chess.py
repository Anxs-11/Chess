import pygame
from showPositions import *



pygame.init()
pygame.display.set_caption("Chess")
screen = pygame.display.set_mode((600, 600))

board = pygame.image.load('Chess Board.jpg')

dark = pygame.image.load('square_dark.jpg')
light = pygame.image.load('square_light.jpg')
dot = pygame.image.load('dot.png')


bb = pygame.image.load('bb.png')
bk = pygame.image.load('bk.png')
bn = pygame.image.load('bn.png')
bp = pygame.image.load('bp.png')
bq = pygame.image.load('bq.png')
br = pygame.image.load('br.png')

wb = pygame.image.load('wb.png')
wk = pygame.image.load('wk.png')
wn = pygame.image.load('wn.png')
wp = pygame.image.load('wp.png')
wq = pygame.image.load('wq.png')
wr = pygame.image.load('wr.png')

TOKENS = [[br, bn, bb, bq, bk, bb, bn, br],
          [bp] * 8,
          [wp] * 8,
          [wr, wn, wb, wq, wk, wb, wn, wr]]


HOME = [[[33 + (67*i), 33 + (67*j)] for i in range(8)] for j in range(2)] + \
       [[[33 + (67*i), 33 + (67*(6+j))] for i in range(8)] for j in range(2)]

dot_coordinates = []

position = HOME


currentPlayer=0

X = 8
Y = 8
CHANGED = False

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(board, (0, 0))
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0:
                screen.blit(dark, (33 + (67*i), 33 + (67*j)))
            else:
                screen.blit(light, (33 + (67*i), 33 + (67*j)))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            CHANGED = False
            coordinates = pygame.mouse.get_pos()
            flag = False
            for i in dot_coordinates:
                if i[0] <= coordinates[0] <= i[0]+67 and i[1] <= coordinates[1] <= i[1]+67:
                    flag = True
                    for j in range(len(position)):
                        for k in range(len(position[j])):
                            if i == position[j][k]:
                                position[j][k] = [1000, 1000]
                                break

                    position[X][Y] = i
                    X = 8
                    Y = 8
                    dot_coordinates = []
                    currentPlayer=(currentPlayer+1)%2
                    break

            if not flag:
                for i in range(len(position)):
                    for j in range(len(position[i])):
                        if position[i][j][0] <= coordinates[0] <= position[i][j][0] + 67 \
                            and position[i][j][1] <= coordinates[1] <= position[i][j][1] + 67:
                            dot_coordinates = []
                            X = i
                            Y = j
                            CHANGED = True

            if not CHANGED:
                X = 8
                Y = 8
                dot_coordinates=[]

    for i in range(len(position)):
        for j in range(len(position[i])):
            screen.blit(TOKENS[i][j], position[i][j])

    if dot_coordinates == [] and ((currentPlayer==1 and (X==0 or X==1)) or (currentPlayer==0 and (X==2 or X==3))):
        show_position(X, Y, position, dot_coordinates)
    else:
        for i in dot_coordinates:
            screen.blit(dot, i)
    pygame.display.update()
