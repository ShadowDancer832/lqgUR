# coding=utf-8
import numpy as np
import scipy.linalg as linalg
import math


old_coor = np.zeros((3, 1), dtype=np.float64)
# old_coor = [1, 0, 0]
old_coor = [0.0125, -0.0146, 0.8]


# 参数分别是旋转轴和旋转弧度值
def rotate_mat(axis, radian):
    rot_matrix = linalg.expm(np.cross(np.eye(3), axis / linalg.norm(axis) * radian))
    return rot_matrix


axis_x, axis_y, axis_z = [1, 0, 0], [0, 1, 0], [0, 0, 1]  # 分别是x,y和z轴,也可以自定义旋转轴
yaw = math.pi/2
print "yaw= "+str(yaw)
rot_matrix = rotate_mat(axis_z, yaw)  # 绕Z轴旋转yaw弧度
new_coor = np.dot(old_coor, rot_matrix)
print "new_coor= "+str(new_coor)
