# -*- encoding: utf-8 -*-
'''
@File    :   ms_模拟面试.py
@Time    :   2022/07/15 22:35:42
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   

青蛙跳。
给定一个 blocks 数组存放了每个 block 的高度。
两只青蛙站在同一个block上，他们吵架了想尽可能地远离对方。
限定他们只能往高处跳(block[next] >= block[current])，可以向左可以向右。
求两只青蛙可以相互远离的最大距离。（青蛙初始block可以选择最优block）

两只青蛙在 L 和 J， J > L 则两者距离为 J - L + 1

[1,2,3] -> 3
[1,1] -> 2
[1,2,1,2,3]  -> 4

'''


from numpy import block


def solution(blocks):
    # write your code in Python 3.6
    max_length = 1
    prev_len, cur_len = 1, 0

    fleft, fright = 0, 0

    while fleft < len(blocks) and fright < len(blocks):
        gap = blocks[fright] - blocks[fleft]

        while fright + 1 < len(blocks):
            temp = blocks[fright + 1] - blocks[fright]
            if gap > 0 and temp >= 0:
                fright += 1
            elif gap < 0 and temp <= 0:
                fright += 1
            elif gap == 0:
                gap = temp
                fright += 1
            else:
                cur_len = fright - fleft + 1
                if gap >= 0:
                    max_length = max(max_length, prev_len + cur_len - 1)
                else:
                    max_length = max(max_length, cur_len)
                prev_len = cur_len
                fleft = fright
                fright += 1
                break
        else:
            cur_len = fright - fleft + 1
            if gap >= 0:
                max_length = max(max_length, prev_len + cur_len - 1)
            else:
                max_length = max(max_length, cur_len)
            break

    return max_length


def solution_dp(blocks):
    dp_up = [1] * len(blocks) # up
    dp_down = [1] * len(blocks) # down
    
    for i in range(1, len(blocks)):
        if blocks[i] >= blocks[i-1]:
            dp_up[i] = dp_up[i-1] + 1
        else:
            dp_up[i] = 1

    for i in range(1, len(blocks)):
        if blocks[i] <= blocks[i-1]:
            dp_down[i] = dp_down[i-1] + 1
        else:
            dp_down[i] = 1
    
    max_len = 0
    for i in range(1, len(blocks)):
        temp = dp_up[i]
        start_idx = i - temp + 1
        max_len = max(dp_down[start_idx] + dp_up[i] - 1, max_len)
    return max_len

if __name__ == "__main__":
    import random
    import time
    
    test_set = [[random.randint(0,100) for _ in range(30)] for _ in range(int(1e5))]

    temp = time.time()
    for test in test_set:
        solution(test)
    print(time.time() - temp)

    temp = time.time()
    for test in test_set:
        solution_dp(test)
    print(time.time() - temp)


    for _ in range(10):
        blocks = [random.randint(0,100) for _ in range(30)]
        if solution(blocks) == solution_dp(blocks):
            print(True)
        else:
            print(blocks)
