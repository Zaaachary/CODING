# -*- encoding: utf-8 -*-
'''
@File    :   DP_01背包.py
@Time    :   2022/07/06 16:35:43
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/circle/article/KPsfIC/
'''

v, w = [0] * 1010, [0] * 1010
f = [[0] * 1010 for i in range(1010)]

N, V = map(int, input().split()) 

for i in range(1, N + 1):
    v[i], w[i] = map(int, input().split())

for i in range(1, N + 1):
    for j in range(1, V + 1):
        f[i][j] = f[i - 1][j]
        if(j >= v[i]): f[i][j] = max(f[i][j], f[i - 1][j - v[i]] + w[i])
print(f[N][V])

