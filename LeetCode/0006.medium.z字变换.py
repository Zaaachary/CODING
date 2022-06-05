# -*- encoding: utf-8 -*-
'''
@File    :   0006.z字变换.py
@Time    :   2022/06/04 20:57:25
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   

将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


from itertools import chain


class Solution:
    '''
    执行用时： 60 ms , 在所有 Python3 提交中击败了 61.37% 的用户 内存消耗： 15.4 MB , 在所有 Python3 提交中击败了 20.67% 的用户
    
    '''
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        mat = [[] for _ in range(numRows)]
        T = numRows + numRows - 2
        for index, ch in enumerate(s):
            index = index % T
            div, mod = divmod(index, numRows)
            if div == 0:    # 竖着下来
                mat[mod].append(ch)
            else:
                mat[numRows - mod - 2].append(ch)

        return ''.join(chain(*mat))
                


### Solution 1  Tree method  超时
class Tree:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.visited = False
    
    def __str__(self) -> str:
        left = self.left if self.left else '_'
        right = self.right if self.right else '_'
        return str(self.val)
        # return str(self.val) + ':[' + str(left) + ';' + str(right) + ']'
    def __call__(self, *args, **kwds):
        return self.val


class Solution_1    :
    '''
    构造树，标记左右方向，迭代后序遍历。
    '''
    def convert(self, s: str, numRows: int) -> str:
        result = []
        
        # build Tree
        queue = []
        root = Tree(-1)
        ptr = root
        left = True
        for index, ch in enumerate(s):
            if left:
                ptr.left = Tree(ch)
                queue.append(ptr.left)
                ptr = ptr.left
            else:
                ptr.right = Tree(ch)
                queue.append(ptr.right)
                ptr = ptr.right
            if numRows == 1:
                pass
            elif index !=0 and index % (numRows-1) == 0:
                left = not left
        while numRows != 1 and index % (numRows-1) != 0:
            if left:
                ptr.left = Tree('')
                queue.append(ptr.left)
                ptr = ptr.left
            else:
                ptr.right = Tree('')
                queue.append(ptr.right)
                ptr = ptr.right
            index += 1

        # Traverse
        prev = None
        while queue:
            # print([item.val for item in queue])
            # print(result)
            # import pdb; pdb.set_trace()
            temp = queue.pop(0)
            # prev 不为 temp 的祖先且 无右节点或右节点已经访问
            # if not prev or prev.right != temp and prev.left != temp:
            if not prev or prev.left != temp:
                if not temp.right or temp.right.visited == True:
                    result.append(temp.val)
                    temp.visited = True
                else:
                    queue.append(temp)
            else:
                queue.append(temp)
            prev = temp

        return ''.join(result)
            
    


if __name__ == "__main__":
    target = "PAYPALISHIRING"
    S = Solution()
    print(S.convert(target,3))