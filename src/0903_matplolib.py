"""
    Time : 2022/09/02
    Author : YU.J.P
    Program : matplotlib
"""
import matplotlib
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


# 测试实例 1
def test01():
    plt.plot([3, 1, 4, 5, 2])
    plt.ylabel("grade")
    plt.savefig('data/plt_png/test01', dpi=600)  # 另存为PNG文件 dpi更改图片质量
    plt.show()


# 测试实例 2
def test02():
    plt.plot([0, 2, 4, 6, 8], [3, 1, 4, 5, 2])  # plot(x, y)
    plt.ylabel("grade")
    plt.axis([-1, 10, 0, 6])  # x y 范围
    plt.savefig('data/plt_png/test02', dpi=600)  # 另存为PNG文件 dpi更改图片质量
    plt.show()


# 能量衰减函数
def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


# 测试实例 3
def test03():
    a = np.arange(0.0, 5.0, 0.02)

    plt.subplot(211)
    plt.plot(a, f(a))

    plt.subplot(2, 1, 2)
    plt.plot(a, np.cos(2 * np.pi * a), 'r--')
    plt.savefig('data/plt_png/test03', dpi=600)  # 另存为PNG文件 dpi更改图片质量
    plt.show()


# 测试实例 pyplot的plot()函数
def plot_1():
    a = np.arange(10)
    plt.plot(a, a * 1.5, 'go-', a, a * 2.5, 'rx', a, a * 3.5, '*', a, a * 4.5, 'b-.')
    plt.show()


"""
matplotlib.rcParams属性
    'font.family'       显示字体的名字 -- 'SimHei'、'Kaiti'、'LiSu'、'FangSong'、'YouYuan'、'STSong'
    'font.style'        字体风格 正常'normal' 斜体'italic'
    'font.size'         字体大小 整数字号 或 'large'、'x-small'
"""
# 测试实例 4 显示汉字
def test04():
    matplotlib.rcParams['font.family'] = 'SimHei'
    plt.plot([3, 1, 4, 5, 2])
    plt.ylabel("纵轴(值)")
    plt.savefig('data/plt_png/test04', dpi=600)  # 另存为PNG文件 dpi更改图片质量
    plt.show()


# 测试实例 5 坐标轴都为汉字显示
def test05():
    matplotlib.rcParams['font.family'] = 'FangSong'  # 设置字体
    matplotlib.rcParams['font.size'] = 20  # 字体大小

    a = np.arange(0.0, 5.0, 0.02)

    plt.xlabel('横轴：时间')
    plt.ylabel('纵轴：振幅')
    plt.plot(a, np.cos(2 * np.pi * a), 'r--')
    # plt.savefig('data/plt_png/test05', dpi=600)  # 另存为PNG文件 dpi更改图片质量
    plt.show()


# 测试实例 6 坐标轴都为汉字显示 第二种方法
def test06():
    a = np.arange(0.0, 5.0, 0.02)

    plt.xlabel('横轴：时间', fontproperties='FangSong', fontsize=20)
    plt.ylabel('纵轴：振幅', fontproperties='FangSong', fontsize=20)
    plt.plot(a, np.cos(2 * np.pi * a), 'r--')
    plt.savefig('data/plt_png/test06', dpi=600)  # 另存为PNG文件 dpi更改图片质量
    plt.show()


# 测试实例 7 pyplot文本显示
def test07():
    a = np.arange(0.0, 5.0, 0.02)
    plt.plot(a, np.cos(2 * np.pi * a), 'r--')

    plt.title(r'正弦波实例 $y=cos(2\pi x)$', fontproperties='SimHei', fontsize=25)
    plt.xlabel('横轴：时间', fontproperties='FangSong', fontsize=20, color='green')
    plt.ylabel('纵轴：振幅', fontproperties='FangSong', fontsize=20, color='blue')
    plt.text(2, 1, r'$\mu=100$', fontsize=15)  # LaTex格式

    plt.axis([-1, 6, -2, 2])
    plt.grid(True)
    plt.savefig('data/plt_png/test07', dpi=600)  # 另存为PNG文件 dpi更改图片质量
    plt.show()


# 测试实例 8 pyplot文本显示 添加箭头
def test08():
    a = np.arange(0.0, 5.0, 0.02)
    plt.plot(a, np.cos(2 * np.pi * a), 'r--')

    plt.title(r'正弦波实例 $y=cos(2\pi x)$', fontproperties='SimHei', fontsize=25)
    plt.xlabel('横轴：时间', fontproperties='FangSong', fontsize=20, color='green')
    plt.ylabel('纵轴：振幅', fontproperties='FangSong', fontsize=20, color='blue')
    # plt.text(2, 1, r'$\mu=100$', fontsize=15)  # LaTex格式
    plt.annotate(r'$\mu=100$',xy=(2, 1), xytext=(3, 1.5),
                 arrowprops=dict(facecolor='pink', shrink=0.1, width=3))

    plt.axis([-1, 6, -2, 2])
    plt.grid(True)
    plt.savefig('data/plt_png/test08', dpi=600)  # 另存为PNG文件 dpi更改图片质量
    plt.show()


# 测试实例 9 pyplt的子绘图区域
def test09():
    plt.subplot2grid((3, 3), (0, 0), colspan=3)
    plt.subplot2grid((3, 3), (1, 0), colspan=2)
    plt.subplot2grid((3, 3), (1, 2), rowspan=2)
    plt.subplot2grid((3, 3), (2, 0))
    plt.subplot2grid((3, 3), (2, 1))
    plt.show()


# 测试实例 10 pyplt的子绘图区域 有误。。。
def test10():

    gs = gridspec.GridSpec(3, 3)

    ax1 = plt.subplots(gs[0, :])
    ax2 = plt.subplots(gs[1, :-1])
    ax3 = plt.subplots(gs[1:, -1])
    ax4 = plt.subplots(gs[2, 0])
    ax5 = plt.subplots(gs[2, 1])

    plt.show()


# pyplot 饼图的绘制
def test11():
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)

    plt.pie(sizes, explode=explode, labels=labels,
            autopct='%1.1f%%', shadow=False, startangle=90)
    plt.axis('equal')

    plt.savefig('data/plt_png/test11', dpi=600)  # 另存为PNG文件 dpi更改图片质量
    plt.show()


# pyplot 直方图的绘制
def test12():
    np.random.seed(0)
    mu, sigma = 100, 20  # 均值和标准差
    a = np.random.normal(mu, sigma, size=100)

    plt.hist(a, bins=20, histtype='stepfilled', facecolor='b', alpha=0.75)
    plt.title('Histogram')

    plt.savefig('data/plt_png/test12', dpi=600)  # 另存为PNG文件 dpi更改图片质量
    plt.show()


# pyplot 极坐标图的绘制
def test13():
    N = 20
    theta = np.linspace(0.0, 2 * np.pi, N, endpoint=False)
    radii = 10 * np.random.rand(N)
    width = np.pi / 4 * np.random.rand(N)

    ax = plt.subplot(111, projection='polar')
    bars = ax.bar(theta, radii, width=width, bottom=0.0)

    for r, bar in zip(radii, bars):
        bar.set_facecolor(plt.cm.viridis(r / 10.))
        bar.set_alpha(0.5)

    plt.savefig('data/plt_png/test13', dpi=600)  # 另存为PNG文件 dpi更改图片质量
    plt.show()


# pyplot 散点图的绘制
def test14():
    fig, ax = plt.subplots()
    ax.plot(10 * np.random.randn(100), 10 * np.random.randn(100), 'o')
    ax.set_title('Simple Scatter')

    plt.savefig('data/plt_png/test14', dpi=600)  # 另存为PNG文件 dpi更改图片质量
    plt.show()



# 运行
if __name__ == '__main__':
    print('# Dealing...')
    # test01()
    # test02()
    # test03()
    # plot_1()
    # test04()
    # test05()
    # test06()
    # test07()
    # test08()
    # test09()
    # test10()
    # test11()
    # test12()
    # test13()
    test14()
    print('# Finished.')
