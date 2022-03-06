# -*- encoding: utf-8 -*-
'''
@File    :   0542.medium.01矩阵.py
@Time    :   2022/03/06 15:50:01
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   超级源点！！
给定一个由 0 和 1 组成的矩阵 mat ，请输出一个大小相同的矩阵，其中每一个格子是 mat 中对应位置元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

'''
from typing import List
from collections import deque

class Solution_fast1:
    '''
    252 ms 76.44% 将所有的0视为超级源点的邻居，将他们首先入队列，然后开始广度优先搜索，给所有的1添加距离。
    '''
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        direction = ((0,1),(0,-1),(1,0),(-1,0))
        distance = [[-1 for _ in range(n)] for _ in range(m)]
        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append((i, j))
                    distance[i][j] = 0
        while queue:
            cur_x, cur_y = queue.popleft()
            for tmp_x, tmp_y in direction:
                tmp_x += cur_x
                tmp_y += cur_y
                if 0 <= tmp_x < m and 0 <= tmp_y < n:
                    if mat[tmp_x][tmp_y] == 1 and distance[tmp_x][tmp_y] == -1:
                        distance[tmp_x][tmp_y] = distance[cur_x][cur_y] + 1
                        queue.append((tmp_x, tmp_y))
        
        return distance

class Solution_dp_fast2:
    """
    动规  从四个方向更新动规矩阵
    作者：LeetCode-Solution
    链接：https://leetcode-cn.com/problems/01-matrix/solution/01ju-zhen-by-leetcode-solution/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    """
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        # 初始化动态规划的数组，所有的距离值都设置为一个很大的数
        dist = [[10**9] * n for _ in range(m)]
        # 如果 (i, j) 的元素为 0，那么距离为 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
        # 只有 水平向左移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向左移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i][j - 1] + 1)
        # 只有 水平向右移动 和 竖直向上移动，注意动态规划的计算顺序
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if i - 1 >= 0:
                    dist[i][j] = min(dist[i][j], dist[i - 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        # 只有 水平向右移动 和 竖直向下移动，注意动态规划的计算顺序
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i + 1 < m:
                    dist[i][j] = min(dist[i][j], dist[i + 1][j] + 1)
                if j + 1 < n:
                    dist[i][j] = min(dist[i][j], dist[i][j + 1] + 1)
        return dist


class Solution_slow1:
    """
    超出时间限制，最后一个样例没有通过
    1. 将1的边缘标记1
    遍历所有 unvisited 的 0，以它们为起点，深度优先搜索0，对于0附近的节点，如果为1则标记其距离为1。
    2. n = 1->x
    遍历所有到0的距离为n的1节点，将相邻的没有距离的1节点标记距离+1
    """
    def __init__(self) -> None:
        self.direction = ((0, 1),(0,-1),(1,0),(-1,0))

    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        self.mat = mat
        self.m, self.n = len(mat), len(mat[0])
        self.distance_mat = [[-1 for _ in range(self.n)] for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if self.mat[i][j] == 0 and self.distance_mat[i][j] == -1:
                    self.BFS_0(i, j)
        
        for distance in range(1, self.m+self.n-1):
            flag = False
            for i in range(self.m):
                for j in range(self.n):
                    if self.mat[i][j] == 1 and self.distance_mat[i][j] == distance:
                        self.BFS_1(i, j, distance)
                        flag = True
            if not flag:
                break

        return self.distance_mat
        
    def BFS_0(self, x, y):
        '''
        标记distance为0，四周零入栈，四周一标记距离1
        '''
        queue = deque([(x, y)])
        self.distance_mat[x][y] = 0
        while queue:
            cur_x, cur_y = queue.popleft()
            for tmp_x, tmp_y in self.direction:
                tmp_x += cur_x
                tmp_y += cur_y
                if 0 <= tmp_x < self.m and 0 <= tmp_y < self.n:
                    if self.mat[tmp_x][tmp_y]:
                        self.distance_mat[tmp_x][tmp_y] = 1
                    elif self.distance_mat[tmp_x][tmp_y] == -1:
                        self.distance_mat[tmp_x][tmp_y] = 0
                        queue.append((tmp_x, tmp_y))

    def BFS_1(self, x, y, distance):
        queue = deque([(x, y)])
        while queue:
            cur_x, cur_y = queue.popleft()
            for tmp_x, tmp_y in self.direction:
                tmp_x += cur_x
                tmp_y += cur_y
                if 0 <= tmp_x < self.m and 0 <= tmp_y < self.n:
                    if self.mat[tmp_x][tmp_y] and self.distance_mat[tmp_x][tmp_y] == distance:
                        self.mat[tmp_x][tmp_y] = 0
                        queue.append((tmp_x, tmp_y))
                    elif self.distance_mat[tmp_x][tmp_y] == -1:
                        self.distance_mat[tmp_x][tmp_y] = distance + 1

class Solution_slow2:
    """
    为每个1进行一次广度优先搜索，寻找最近0
    """
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        for i, row in enumerate(matrix):
            result.append([])
            for j, num in enumerate(row):
                if num == 0:
                    result[i].append(num)
                else:
                    # 找到到最近0的距离
                    d = self.find_x(i, j, matrix)
                    result[i].append(d)
        return result

    def find_x(self, i, j, matrix):
        if i == 2 and j ==2:
            print('!')
        dis = 0
        i_t, j_t = i, j
        step, dirc = 0, 3
        dirction = ((-1, -1), (-1, 1), (1, 1), (1, -1))
        while True:
            if 0 <= i_t < len(matrix) and 0 <= j_t < len(matrix[0]) \
                    and matrix[i_t][j_t] == 0:
                return dis
            else:
                if step < dis:
                    # 走一侧
                    i_t += dirction[dirc][0]
                    j_t += dirction[dirc][1]
                    step += 1
                elif dirc < 3:
                    # 换方向
                    step = 0
                    dirc += 1
                else:
                    # 换一圈
                    dis += 1
                    step, dirc = 0, 0
                    i_t, j_t = i + dis, j

if __name__ == "__main__":
    S = Solution()
    mat = [[0,0,0,1],[0,1,0,1],[1,1,1,0]]
    print(S.updateMatrix(mat))