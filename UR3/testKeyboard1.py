# coding=utf-8

import pygame
from pygame.locals import *

pygame.init()

while True:
    for event in pygame.event.get():
        # 判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        # 判断是否是按下了键
        elif event.type == KEYDOWN:
            # 检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
            # 检测按键是否是d或者right
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
            # 检测按键是否是w或者up
            elif event.key == K_w or event.key == K_UP:
                print("up")
            # 检测按键是否是s或者down
            elif event.key == K_s or event.key == K_DOWN:
                print("down")
            # 检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
