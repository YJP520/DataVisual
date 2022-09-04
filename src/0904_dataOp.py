"""
    Time : 2022/09/04
    Author : YU.J.P
    Program : 数据的基本处理
"""

"""
    .sort_index(axis=0, ascending=True)  默认升序排序
    .sort_values(by, axis=0, ascending=True)  默认升序排序
"""

import numpy as np
import pandas as pd


# 测试实例 1
def test01():
    b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['c', 'a', 'd', 'b'])
    print(b)
    print(b.sort_index())
    print(b.sort_index(ascending=False))  # 降序排序


# 测试实例 2
def test02():
    b = pd.DataFrame(np.arange(20).reshape(4, 5), index=['c', 'a', 'd', 'b'])
    print(b)
    print(b.sort_values(2, ascending=False))  # 降序排序
    print(b.sort_values('a', axis=1, ascending=False))  # 降序排序


# 测试实例 3
def test03():
    a = pd.DataFrame(np.arange(20).reshape(4, 5), index=['c', 'a', 'd', 'b'])
    print(a.describe())


# 测试实例 4
def test04():
    a = pd.DataFrame(np.arange(20).reshape(4, 5), index=['c', 'a', 'd', 'b'])
    print(a.cumsum())
    print(a.cumprod())
    print(a.cummax())
    print(a.cummin())
    print(a.rolling(2).sum())


# 测试实例 5 Pearson相关系数
def test05():
    pass


if __name__ == '__main__':
    print('# Dealing...')
    # test01()
    # test02()
    # test03()
    test04()
    # test05()
    # test06()
    # test07()
    # test08()
    # test09()
    # test10()
    # test11()
    print('# Finished.')
