/*
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

*/

class Solution_1 {
    // 递归，超时
public:
    int climbStairs(int n) {
        if (n <= 0)
            return 0;
        else if (n == 1)
            return 1;
        else if (n == 2)
            return 2;
        else{
            return climbStairs(n-1) + climbStairs(n-2);
        }
    }
};

class Solution_2 {
    // 自底向上的动态规划
    // 执行用时： 0 ms , 在所有 C++ 提交中击败了 100.00% 的用户 内存消耗： 5.8 MB , 在所有 C++ 提交中击败了 75.47% 的用户
public:
    int climbStairs(int n) {
        if (n <= 2)
            return n;
        int j = 1, k = 2; // no1, no2
        int temp = -1;
        while (n > 2){
            temp = k;
            k = j + k;
            j = temp;
            n--;
        }
        return k;
    }
};