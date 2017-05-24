#!/usr/bin/python
# coding:utf-8

import random as random

import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


# 实验
class Experiment:
    def __init__(self, icon):
        self.icon = icon

    def start(self, n):  # 投掷n次
        res = ThrowResult()
        for index in range(0, n):
            if self.icon.throw() == 1:
                res.positive += 1
            else:
                res.negative += 1
        return res


# 具有不同概率的硬币
class Icon:
    def __init__(self, positive=0.5):
        self.totalCount = 100  # 总的随机数
        self.splitPoint = self.totalCount * positive

    # 投掷，正面返回1，反面返回0
    def throw(self):
        rand = random.randint(0, 99)  #
        return 1 if rand < self.splitPoint else 0


# 投掷的结果
class ThrowResult:
    def __init__(self):
        self.positive = 0  # 正面次数
        self.negative = 0  # 反面次数

    # 正面朝上的概率，精确到0.1
    def probability(self):
        return 0 if self.positive == self.negative == 0 else round(
            self.positive * 10 / (self.positive + self.negative)) / 10


# 投掷的结果
arr = []

# 每次实验投掷的次数
n = 1000

# 重复2000次实验
for i in range(1, 2000):
    # 不公平的硬币
    # icon = Icon(0.9)

    # 公平的硬币
    icon = Icon()

    experiment = Experiment(icon)
    r = experiment.start(n)
    arr.append(r.positive)

print(arr)

# 绘图时分割线, 以5为间隔
bins = []
bin = 0
while bin <= n:
    bins.append(bin)
    bin += 5

# 绘制直方图
plt.hist(arr, bins)
plt.xlabel(u'正面朝上的次数')
# plt.ylabel('COUNT')
plt.title(u'概率密度直方图')
plt.grid(True)

plt.show()
