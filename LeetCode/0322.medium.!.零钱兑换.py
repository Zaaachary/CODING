# -*- encoding: utf-8 -*-
'''
@File    :   0322.medium.零钱兑换.py
@Time    :   2022/07/16 14:25:50
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/coin-change/

https://www.programmercarl.com/0322.%E9%9B%B6%E9%92%B1%E5%85%91%E6%8D%A2.html#%E6%80%9D%E8%B7%AF

本题求钱币最小个数，那么钱币有顺序和没有顺序都可以，都不影响钱币的最小个数。

所以本题并不强调集合是组合还是排列。

如果求组合数就是外层for循环遍历物品，内层for遍历背包。

如果求排列数就是外层for遍历背包，内层for循环遍历物品。

在动态规划专题我们讲过了求组合数是动态规划：518.零钱兑换II (opens new window)，求排列数是动态规划：377. 组合总和 Ⅳ (opens new window)。
'''
class Solution_dp:
    '''
    完全背包问题，类似走楼梯，区别是有多种步长，且有的台阶不会走到。
    执行用时： 1200 ms , 在所有 Python3 提交中击败了 72.11% 的用户 内存消耗： 15.4 MB , 在所有 Python3 提交中击败了 26.90% 的用户
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1) # dp[j]：凑足总额为j所需钱币的最少个数为dp[j]
        dp[0] = 0
        # print(dp)
        for coin in coins:
            for idx in range(coin, len(dp)):
                if dp[idx - coin] != amount + 1:
                    dp[idx] = min(dp[idx], dp[idx-coin] + 1)
                # print(coin, idx, dp)
        
        if dp[amount] != amount + 1:
            return dp[amount]
        else:
            return -1



class Solution_backtracing:
    '''
    回溯法，遍历所有可能的硬币组合，超时。
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)

        coin_count = int(1e4) + 1
        current_amount = amount
        current_coin_count = 0

        def back_tracing(coin_idx):
            nonlocal current_amount, coin_count, current_coin_count
            if current_amount == 0:
                coin_count = min(coin_count, current_coin_count)
            elif 0 <= coin_idx <len(coins):
                select_coin = coins[coin_idx]
                for num in range(current_amount // select_coin, -1, -1):
                    current_amount -= num * select_coin
                    current_coin_count += num
                    back_tracing(coin_idx + 1)
                    current_coin_count -= num
                    current_amount += num * select_coin
        back_tracing(0)
        return coin_count if coin_count != int(1e4) + 1 else -1


from functools import cache

class Solution_2_memory:
    '''
    动态规划思想  记忆化搜索
    执行用时： 1152 ms , 在所有 Python3 提交中击败了 82.57% 的用户 内存消耗： 35.5 MB , 在所有 Python3 提交中击败了 7.91% 的用户
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:

        @cache
        def change(amount):
            # amount 金额下最少需要多少硬币
            nonlocal coins
            if amount == 0:
                return 0
            elif amount < 0:
                return -1
            else:
                min_coin_count = amount + 1
                for coin in coins:
                    result = change(amount - coin) + 1
                    if result:  # change(amount - coin) != 0
                        min_coin_count = min(min_coin_count, result)
                
                return min_coin_count if min_coin_count != amount + 1 else -1


        return change(amount)






'''
class Solution {
    vector<int>count;
    int dp(vector<int>& coins, int rem) {
        if (rem < 0) return -1;
        if (rem == 0) return 0;
        if (count[rem - 1] != 0) return count[rem - 1];
        int Min = INT_MAX;

        // notice type xxx:xxxs
        for (int coin:coins) {

            int res = dp(coins, rem - coin);
            if (res >= 0 && res < Min) {
                Min = res + 1;
            }
        }
        count[rem - 1] = Min == INT_MAX ? -1 : Min;
        return count[rem - 1];
    }
public:
    int coinChange(vector<int>& coins, int amount) {
        if (amount < 1) return 0;
        count.resize(amount);
        return dp(coins, amount);
    }
};

'''