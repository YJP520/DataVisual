"""
    Time : 2022/09/03
    Author : YU.J.P
    Program : pandas库 Series DatFrame
"""
import matplotlib
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import pandas as pd


# 测试实例 1
def test01():
    d = pd.Series(range(20))
    print(d)
    print(d.cumsum())  # 前n项和


# 测试实例 2 Series
def test02():
    d = pd.Series([10, 20, 30, 40], ['a', 'b', 'c', 'd'])
    print(d)
    print(d.index)  # .index 获得索引
    print(d.values)  # .values 获得数据


# 测试实例 3
def test03():
    b = pd.Series([10, 20, 30, 40], ['a', 'b', 'c', 'd'])
    print(b['b'])
    print('c' in b)
    print('0' in b)
    print(b.get('f', 100))  # 无 f 返回第二个参数


# 测试实例 4
def test04():
    b = pd.Series([10, 20, 30, 40], ['a', 'b', 'c', 'd'])
    b.name = 'Series对象'
    b.index.name = '索引列'
    print(b)


# 测试实例 5 DataFrame类型 横向 纵向的索引
def test05():
    d = pd.DataFrame(np.arange(10).reshape(2, 5))
    print(d)


# 测试实例 6 DataFrame类型 横向 纵向的索引
def test06():
    dt = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
          'two': pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])}
    d2 = pd.DataFrame(dt)
    print(d2)


# 测试实例 7 DataFrame类型 横向 纵向的索引
def test07():
    dt = {'one': pd.Series([1, 2, 3], index=['a', 'b', 'c']),
          'two': pd.Series([9, 8, 7, 6], index=['a', 'b', 'c', 'd'])}
    d2 = pd.DataFrame(dt, index=['b', 'c', 'd'], columns=['two', 'three'])
    print(d2)


# 测试实例 8 DataFrame类型 横向 纵向的索引
def test08():
    dl = {'one': [1, 2, 3, 4], 'two': [9, 8, 7, 6]}
    d = pd.DataFrame(dl, index=['a', 'b', 'c', 'd'])
    print(d)


# 测试实例 9 .reindex 重排索引
def test09():
    dl = {'one': [1, 2, 3, 4], 'two': [9, 8, 7, 6]}
    d = pd.DataFrame(dl, index=['a', 'b', 'c', 'd'])
    print(d)
    d = d.reindex(columns=['城市', '同比', 'one', 'two'], fill_value=0)
    print(d)
    newc = d.columns.insert(4, '新增')
    newd = d.reindex(columns=newc, fill_value=200)
    print(newd)


# 测试实例 10
def test10():
    a = pd.Series([10, 20, 30, 40], ['a', 'b', 'c', 'd'])
    print(a.drop(['b']))


# 测试实例 11
def test11():
    a = pd.Series([10, 20, 30, 40], ['a', 'b', 'c', 'd'])
    b = pd.Series([30, 50, 70, 90], ['a', 'b', 'c', 'd'])
    print(a + b)
    print(b.add(a))
    print(a + 100)
    print(b.add(a, axis=0))
    print(a > b)


if __name__ == '__main__':
    print('# Dealing...')
    # test01()
    # test02()
    # test03()
    # test04()
    # test05()
    # test06()
    # test07()
    # test08()
    # test09()
    # test10()
    test11()
    print('# Finished.')
