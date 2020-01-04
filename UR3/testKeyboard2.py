# coding=utf-8

import pygame
from pygame.locals import *
from sys import exit

background_image_file = 'front2.png'

pygame.init()
pygame.display.set_caption("Sugar")
screen = pygame.display.set_mode((500, 500), FULLSCREEN, 32)
background = pygame.image.load(background_image_file).convert()

x, y = 0, 0
move_x, move_y = 0, 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                move_x = -1
                print('left')
            elif event.key == K_RIGHT:
                move_x = 1
                print('right')
            elif event.key == K_UP:
                move_y = -1
                print('up')
            elif event.key == K_DOWN:
                move_y = 1
                print('down')
            elif event.key == K_SPACE:
                exit()
                print('space')
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0

            # 计算新的坐标
    x += move_x
    y += move_y

    screen.fill((0, 0, 0))
    screen.blit(background, (x, y))
    pygame.display.update()
