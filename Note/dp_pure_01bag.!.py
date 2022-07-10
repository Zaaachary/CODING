# -*- encoding: utf-8 -*-
'''
@File    :   DP_01背包.py
@Time    :   2022/07/06 16:35:43
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://www.programmercarl.com/%E8%83%8C%E5%8C%85%E7%90%86%E8%AE%BA%E5%9F%BA%E7%A1%8001%E8%83%8C%E5%8C%85-1.html
有n件物品和一个最多能背重量为w 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。每件物品只能用一次，求解将哪些物品装入背包里物品价值总和最大。

就是本文中的题目，要求先实现一个纯二维的01背包，如果写出来了，然后再问为什么两个for循环的嵌套顺序这么写？反过来写行不行？再讲一讲初始化的逻辑。

然后要求实现一个一维数组的01背包，最后再问，一维数组的01背包，两个for循环的顺序反过来写行不行？为什么？

注意以上问题都是在候选人把代码写出来的情况下才问的。

就是纯01背包的题目，都不用考01背包应用类的题目就可以看出候选人对算法的理解程度了。

相信大家读完这篇文章，应该对以上问题都有了答案！

此时01背包理论基础就讲完了，我用了两篇文章把01背包的dp数组定义、递推公式、初始化、遍历顺序从二维数组到一维数组统统深度剖析了一遍，没有放过任何难点。

'''


from re import S


def bag(weight, value, bag_size):
    '''
    dp[i][j] 有 j 空间时候, 0~i 个物品可以装的最大值。
    边界条件 dp[0][i] = value[i] if weight[i] < bag_size else 0; dp[all][0] = 0
    dp[i][j] = dp[i-1]
    max(不放当前物品的价值，放当前物品的价值 + 剩下空间的价值)
    dp[i][j] = max(dp[i-1][j], value[i]+dp[i-1][j-weight[i]])
    '''
    if bag_size <= 0:
        return 0

    n = len(value)
    dp = [[0] * (bag_size+1) for _ in range(n)] 
    # j 大于 weight[0] 的时候赋第一个物品的价值
    for j in range(weight[0], bag_size+1):
        dp[0][j] = value[0]
    print(dp)

    # 先遍历物品，再遍历包的尺寸
    for j in range(1, bag_size+1):
        for i in range(1, n):
            if weight[i] > j:
                # 当前物品放不下
                dp[i][j] = dp[i-1][j]
            else:
                # max(不放当前物品的价值，放当前物品的价值 + 剩下空间放旧物品的最大价值)
                dp[i][j] = max(dp[i-1][j], value[i]+dp[i-1][j-weight[i]])
            print(dp)
    
    return dp[-1][-1]

def bag_rolling_array(weight, value, bag_size):
    if bag_size <= 0 or len(value) <= 0:
        return 0
    n = len(value)
    dp = [0] * (bag_size+1)
    
    # 初始化，空间大于第一个物品大小，则赋value
    for j in range(weight[0], bag_size+1):
        dp[j] = value[0]
    
    for i in range(n):
        for j in range(bag_size, weight[i], -1):
            if weight[i] <= j:
                dp[j] = max(dp[j], value[i] + dp[j - weight[i]])    # j - weight[i] 得 大于0
            # else:
                # dp[j] = dp[j]

    return dp[-1]




if __name__ == "__main__":
    weight = [1, 3, 4]
    value = [15, 20, 30]
    print(bag_rolling_array(weight, value, 4))