# -*- encoding: utf-8 -*-
'''
@File    :   0733.图像渲染.py
@Time    :   2022/02/22 21:30:26
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   
有一幅以二维整数数组表示的图画，每一个整数表示该图画的像素值大小，数值在 0 到 65535 之间。

给你一个坐标 (sr, sc) 表示图像渲染开始的像素值（行 ，列）和一个新的颜色值 newColor，让你重新上色这幅图像。

为了完成上色工作，从初始坐标开始，记录初始坐标的上下左右四个方向上像素值与初始坐标相同的相连像素点，接着再记录这四个方向上符合条件的像素点与他们对应四个方向上像素值与初始坐标相同的相连像素点，……，重复该过程。将所有有记录的像素点的颜色值改为新的颜色值。

最后返回经过上色渲染后的图像。
'''
from typing import List

class Solution:
    '''
    非递归广度优先遍历  32ms 85.98%
    '''
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if newColor == old_color:
            return image
        directions = [(1, 0),(-1, 0),(0, 1),(0, -1)]

        visit_queue = [(sr, sc)]
        while visit_queue:
            cur_r, cur_c = visit_queue.pop(0)
            image[cur_r][cur_c] = newColor
            for r, c in directions:
                neighbor_r = cur_r + r
                neighbor_c = cur_c + c
                if 0 <= neighbor_r < len(image) and 0 <= neighbor_c < len(image[0]) and image[neighbor_r][neighbor_c] == old_color:
                    visit_queue.append((neighbor_r, neighbor_c))
        
        return image
            

class Solution_visited:
    '''
    非递归广度优先遍历 with visited 44ms 16.31%
    '''
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        old_color = image[sr][sc]
        if newColor == old_color:
            return image
        directions = [(1, 0),(-1, 0),(0, 1),(0, -1)]

        visit_queue = [(sr, sc)]
        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
        while visit_queue:
            cur_r, cur_c = visit_queue.pop(0)
            visited[cur_r][cur_c] = True
            if image[cur_r][cur_c] == old_color:
                image[cur_r][cur_c] = newColor
                for r, c in directions:
                    neighbor_r = cur_r + r
                    neighbor_c = cur_c + c
                    if 0 <= neighbor_r < len(image) and 0 <= neighbor_c < len(image[0]) and not visited[neighbor_r][neighbor_c]:
                        visit_queue.append((neighbor_r, neighbor_c))
        
        return image
            