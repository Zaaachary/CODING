# -*- encoding: utf-8 -*-
'''
@File    :   0413.medium.等差数列个数.py
@Time    :   2022/06/26 20:34:50
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
如果一个数列 至少有三个元素 ，并且任意两个相邻元素之差相同，则称该数列为等差数列。

例如，[1,3,5,7,9]、[7,7,7,7] 和 [3,-1,-5,-9] 都是等差数列。
给你一个整数数组 nums ，返回数组 nums 中所有为等差数组的 子数组 个数。

子数组 是数组中的一个连续序列。

 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/arithmetic-slices
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution_leetcode_dp(object):
    '''
    执行用时： 32 ms , 在所有 Python3 提交中击败了 93.26% 的用户 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 55.26% 的用户
    动态规划
    上面的递归的解法，是「自顶向下」的思路。如果转成「自底向上」的思路，就变成了动态规划。

    类似于递归解法，我们定义 dp[i]dp[i] 是以 A[i]A[i] 为终点的等差数列的个数。
    ​

    类似于上面的递归思路，有两种情况：
    ​

    A[i] - A[i - 1] == A[i - 1] - A[i - 2]时，说明增加的A[i]能和前面构成等差数列，那么 dp[i] = dp[i - 1] + 1；
    A[i] - A[i - 1] != A[i - 1] - A[i - 2]时， 说明增加的 A[i]不能和前面构成等差数列，所以dp[i] = 0；
    动态规划的初始状态：dp[0] = 0, dp[1] = 0dp[0]=0,dp[1]=0。
    ​

    最后，我们要求的是整个数组中的等差数列的数目，所以需要把 0 <= i <= len(A - 1)0<=i<=len(A−1) 的所有 dp[i]dp[i] 的结果累加起来。

    作者：fuxuemingzhu
    链接：https://leetcode.cn/problems/arithmetic-slices/solution/fu-xue-ming-zhu-bao-li-shuang-zhi-zhen-d-fc1l/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''
    def numberOfArithmeticSlices(self, A):
        N = len(A)
        dp = [0] * N
        for i in range(1, N - 1):
            if A[i - 1] + A[i + 1] == A[i] * 2:
                dp[i] = dp[i - 1] + 1
        return sum(dp)


class Solution:
    '''
    类似动规 比较 i~j 的思路，但无需遍历所有的可能
    (i, j-1)是等差 && nums[j] - nums[j-1] = gap 则 (i, j) 是等差
    执行用时： 36 ms , 在所有 Python3 提交中击败了 78.59% 的用户 内存消耗： 15.2 MB , 在所有 Python3 提交中击败了 37.29% 的用户
    '''
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        result = 0 
        for i in range(0, len(nums) - 2):
            gap = nums[i+1] - nums[i]
            for j in range(i + 2, len(nums)):
                if nums[j] - nums[j-1] == gap:
                    result += 1
                else:
                    break
        
        return result
