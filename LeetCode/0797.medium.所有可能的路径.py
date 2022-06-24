# -*- encoding: utf-8 -*-
'''
@File    :   0797.medium.所有可能的路径.py
@Time    :   2022/06/23 11:49:17
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   

给你一个有 n 个节点的 有向无环图（DAG），请你找出所有从节点 0 到节点 n-1 的路径并输出（不要求按特定顺序）

 graph[i] 是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点 graph[i][j]存在一条有向边）。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/all-paths-from-source-to-target
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    '''
    执行用时： 48 ms , 在所有 Python3 提交中击败了 57.88% 的用户 内存消耗： 16.3 MB , 在所有 Python3 提交中击败了 27.55% 的用户
    '''
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.result = []
        self.graph = graph
        self.target = len(graph) - 1
        self.current_path = []
        self.visited = [False] * len(graph)
        self.DFS()
        
        return self.result
        
    def DFS(self, i=0):
        self.current_path.append(i)
        self.visited[i] = True
        if i == self.target:
            self.result.append(self.current_path[:])
        else:
            for j in self.graph[i]:
                if not self.visited[j]:
                    self.DFS(j)
    
        self.visited[i] = False
        self.current_path.pop()
            