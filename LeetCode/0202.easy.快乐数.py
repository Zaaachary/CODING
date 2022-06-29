# -*- encoding: utf-8 -*-
'''
@File    :   0202.easy.快乐数.py
@Time    :   2022/06/26 15:46:35
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」 定义为：

对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/happy-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    '''
    哈希表 检测重复
    执行用时： 32 ms , 在所有 Python3 提交中击败了 96.88% 的用户 内存消耗： 14.8 MB , 在所有 Python3 提交中击败了 73.13% 的用户
    '''
    def isHappy(self, n: int) -> bool:

        target_set = set([2])
        target = n
        while True:
            new_target = 0
            while target:
                target, temp = divmod(target, 10)
                new_target += temp ** 2
            if new_target == 1:
                return True
            elif new_target in target_set:
                return False
            else:
                target = new_target
                target_set.add(target)


