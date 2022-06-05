# -*- encoding: utf-8 -*-
'''
@File    :   0231.2的幂.py
@Time    :   2022/06/05 21:47:41
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   

给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2x ，则认为 n 是 2 的幂次方。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    '''
    执行用时： 32 ms , 在所有 Python3 提交中击败了 92.62% 的用户 内存消耗： 15 MB , 在所有 Python3 提交中击败了 16.32% 的用户
    从 0~∞ 遍历 2**x 直到不小于n
    '''
    def isPowerOfTwo(self, n: int) -> bool:
        temp = 1
        while n > temp:
            temp = temp << 1
            
        return True if temp == n else False

if __name__ == "__main__":
    S = Solution()
    print(S.isPowerOfTwo(2**12))