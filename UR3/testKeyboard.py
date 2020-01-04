# coding=utf-8
from time import sleep
import pygame
from pygame.locals import *
from sys import exit
import socket

HOST = "192.168.1.2"    # The remote host
PORT = 30003        # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
# 运动到初始位置;
strL1 = b"movej(p[-0.10,-0.10,0.50,0.0125,-0.0146,0.8],a=0.5,v=0.3)\n"
s.send(strL1)
sleep(5)

background_image_file = 'front2.png'
pygame.init()
pygame.display.set_caption("Sugar")
screen = pygame.display.set_mode((500, 500), FULLSCREEN, 32)
background = pygame.image.load(background_image_file).convert()

x, y, z, rx, ry, rz = -0.10, -0.10, 0.50, 0.0125, -0.0146, 0.8
move_x, move_y, move_z, move_rx, move_ry, move_rz = 0, 0, 0, 0, 0, 0
flag = 1

while True:
    sleep(0.01)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            flag = 1
            if event.key == K_LEFT:  # 左平移
                move_y = -0.001
                print('左')
            elif event.key == K_RIGHT:  # 右平移
                move_y = 0.001
                print('右')
            elif event.key == K_UP:  # 前进
                move_x = 0.001
                print('前')
            elif event.key == K_DOWN:  # 后退
                move_x = -0.001
                print('后')
            elif event.key == K_KP8:  # 上升
                move_z = 0.001
                print('上升')
            elif event.key == K_KP2:  # 下降
                move_z = -0.001
                print('下降')

            if event.key == K_q:  # 逆时针转头(翻滚)
                move_rz = -0.001
                print('左转')
            elif event.key == K_e:  # 顺时针转头(翻滚)
                move_rz = 0.001
                print('右转')
            elif event.key == K_a:  # 左旋转(偏航)
                move_ry = -0.001
                print('左转')
            elif event.key == K_d:  # 右旋转(偏航)
                move_ry = 0.001
                print('右转')
            elif event.key == K_w:  # 上仰
                move_rx = 0.001
                print('上升')
            elif event.key == K_s:  # 下俯
                move_rx = -0.001
                print('下降')

            elif event.key == K_SPACE:
                print('Home')
                x, y, z, rx, ry, rz = -0.10, -0.10, 0.50, 0.0125, -0.0146, 0.8
                s.send(strL1)

            elif event.key == K_ESCAPE:
                print('escape')
                exit()
        elif event.type == KEYUP:
            move_x = 0
            move_y = 0
            move_z = 0
            move_rx = 0
            move_ry = 0
            move_rz = 0
            flag = 0

    # 计算新的坐标
    x += move_x
    y += move_y
    z += move_z
    rx += move_rx
    ry += move_ry
    rz += move_rz

    strL2 = b"movej(p["+str(x)+","+str(y)+","+str(z)+","+str(rx)+","+str(ry)+","+str(rz)+"])\n"
    if flag == 1:
        s.send(strL2)

    screen.fill((0, 0, 0))
    screen.blit(background, (x, y))
    pygame.display.update()
s.close()
