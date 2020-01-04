# -*- coding: utf-8 -*-
import socket
import ctypes

# 调用c++动态链接库
from rospy import sleep

so = ctypes.cdll.LoadLibrary
lib = so("/home/lqg/KDevProjects/CohandDriver/lib.so")
# libdri = so("/home/lqg/KDevProjects/CohandDriver/libdri.so")
# libsys = so("/home/lqg/KDevProjects/CohandDriver/libsys.so")
# lib_ = so("/home/lqg/KDevProjects/CohandDriver/lib_.so")
# lib = ctypes.CDLL("/home/lqg/KDevProjects/CohandDriver/lib.so")

# socket连接（主机ip需改为192.168.1.1）
HOST = "192.168.1.2"    # The remote host
PORT = 30003        # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

# 6个参数是[x,y,z,rx,ry,rz];
strL1 = b"movej(p[-0.10,-0.10,0.50,0.0125,-0.0146,0.8],a=0.5,v=0.3)\n"

strL2 = b"movej(p[-0.2,-0.3,0.4,-0.08,-1.57,0.13],a=0.5,v=0.3)\n"

strHover = b"movej(p[-0.380,-0.0188,0.443,-2.9179,-1.016,0.0858],a=0.5,v=0.3)\n"    #悬停位置
strGrasp1 = b"movej(p[-0.399,-0.012,0.250,-3.12,0.083,0.068],a=0.5,v=0.3)\n"    #抓取位置1
strGrasp2 = b"movej(p[-0.393,0.041,0.401,2.868,0.703,-0.054],a=0.5,v=0.3)\n"    #抓取位置2
# strL2 = b"movej(p[-0.143,-0.435,0.200,0.001,-3.166,-0.04],a=0.5,v=0.3)\n"  # 加上“b”表示发送的是bytes型而不是str型

# 动作
lib.openPort()
s.send(strHover)
sleep(7)
s.send(strGrasp2)
sleep(3)

lib.threeFGrasp(200)
sleep(1)
# lib.loosen()
s.send(strL1)
sleep(10)

s.send(strHover)
sleep(7)
s.send(strGrasp2)
sleep(3)
lib.threeFLoosen()
sleep(1)
s.send(strHover)
sleep(3)
s.send(strL1)

s.close()


# 抓手测试

# lib.openPort()
# lib.pose(800)
# sleep(1)
# lib.threeFGrasp(200)
# sleep(1)
# lib.threeFLoosen()
# lib.threeFLoosen()
# sleep(1)
#


# lib.threeFGrasp(200)
# sleep(1)
# lib.threeFLoosen()
# sleep(1)
#
# lib.threeFGrasp(300)
# sleep(1)
# lib.threeFLoosen()
# sleep(1)
#
#
# lib.twoFGrasp(100)
# sleep(1)
# lib.twoFLoosen()
# sleep(1)
#
# lib.twoFGrasp(200)
# sleep(1)
# lib.twoFLoosen()
# sleep(1)
#
# lib.twoFGrasp(300)
# sleep(1)
# lib.twoFLoosen()
# sleep(1)
