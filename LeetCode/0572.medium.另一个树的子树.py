"""

给定两个非空二叉树 s 和 t，检验 s 中是否包含和 t 具有相同结构和节点值的子树。
s 的一个子树包括 s 的一个节点和这个节点的所有子孙。s 也可以看做它自身的一棵子树。

其他方法：哈希树、先序遍历 (空子改为leftnull 或者 rightnull)
https://leetcode.cn/problems/subtree-of-another-tree/solution/ling-yi-ge-shu-de-zi-shu-by-leetcode-solution/
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    '''
    执行用时： 124 ms , 在所有 Python3 提交中击败了 41.56% 的用户 内存消耗： 15.7 MB , 在所有 Python3 提交中击败了 90.50% 的用户
    '''
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        stack = []
        stack.append(root)

        while stack:
            temp = stack.pop()
            if temp:
                if self.areSame(temp, subRoot):
                    return True
                else:
                    stack.append(temp.left)
                    stack.append(temp.right)

        return False

    @staticmethod
    def areSame(t1, t2):
        if not t1 and not t2:
            return True
        elif not (t1 and t2) or t1.val != t2.val:
            return False
        else:
            return Solution.areSame(t1.left, t2.left) and Solution.areSame(t1.right, t2.right)


if __name__ == "__main__":
    pass