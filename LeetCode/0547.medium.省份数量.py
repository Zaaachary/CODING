# -*- encoding: utf-8 -*-
'''
@File    :   0547.medium.省份数量.py
@Time    :   2022/06/20 21:41:29
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''

class Solution:
    '''
    执行用时： 40 ms , 在所有 Python3 提交中击败了 97.01% 的用户 内存消耗： 15.2 MB , 在所有 Python3 提交中击败了 72.89% 的用户
    '''
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.isConnected = isConnected
        self.n = len(isConnected)
        self.visited = [False] * self.n
        province_count = 0
        for target in range(self.n):
            if not self.visited[target]:
                province_count += 1
                self.DFS(target)
        return province_count

    def DFS(self, target):
        self.visited[target] = True
        for index, connect in enumerate(self.isConnected[target]):
            if connect and not self.visited[index]:
                self.DFS(index)

        
