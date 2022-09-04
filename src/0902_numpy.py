"""
    Time : 2022/09/02
    Author : YU.J.P
    Program : 数据可视化
"""
import numpy as np


# 普通计算方式
def pySum():
    a = [0, 1, 2, 3, 4]
    b = [9, 8, 7, 6, 5]
    c = []
    for i in range(len(a)):
        c.append(a[i] ** 2 + b[i] ** 3)
    return c


# numpy计算方式
def npSum():
    a = np.array([0, 1, 2, 3, 4])
    b = np.array([9, 8, 7, 6, 5])
    c = a ** 2 + b ** 3
    return c


# ndarray 对象的属性
def ndarray():
    nd = npSum()

    print(nd.ndim)  # 秩，即轴的数量或维度的数量
    print(nd.shape)  # ndarray对象的尺度，对于矩阵，n行m列
    print(nd.size)  # ndarray对象的个数，相当于.shape.中n*m的值
    print(nd.dtype)  # ndarray对象的元素类型
    print(nd.itemsize)  # ndarray对象中每个元素的大小，以字节为单位


if __name__ == "__main__":
    print(pySum())
    print(npSum())
    ndarray()