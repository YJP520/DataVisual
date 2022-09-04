"""
    Time : 2022/09/02
    Author : YU.J.P
    Program : 图像的手绘效果 -- 效果感人...
"""

from PIL import Image
import numpy as np


def imageToHandPainted():
    image_name = input('# xxx.jpg : ')
    image_array = np.asarray(Image.open('data/image/' + image_name).convert('L')).astype('float')

    depth = 15.  # 深度 范围 0 - 100

    grad = np.gradient(image_array)  # 获取图像灰度的梯度值
    grad_x, grad_y = grad
    grad_x = grad_x * depth / 100.  # 分别取横纵图像梯度值
    grad_y = grad_y * depth / 100.
    value = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
    uni_x = grad_x / value
    uni_y = grad_y / value
    uni_z = 1. / value

    vec_el = np.pi / 2.2  # 光源的俯视角度，弧度值
    vec_az = np.pi / 4.  # 光源的方位角度，弧度值
    dx = np.cos(vec_el) * np.cos(vec_az)  # 光源对x轴的影响
    dy = np.cos(vec_el) * np.sin(vec_az)  # 光源对y轴的影响
    dz = np.sin(vec_el)  # 光源对z轴的影响

    new_image_array = 255 * (dx * uni_x + dy * uni_y + dz * uni_z)  # 光源归一化
    new_image_array = new_image_array.clip(0, 255)

    new_image = Image.fromarray(new_image_array.astype('uint8'))  # 重构图像
    new_image.save('data/image/' + image_name[0: -4] + 'HP.jpg')


# 运行
if __name__ == '__main__':
    print('# Dealing...')
    imageToHandPainted()
    print('# Finished.')