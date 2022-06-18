float('inf')
float('-inf')

from collections import Counter
c_d = Counter(nums)
c_d.most_common(1)[0][0]

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        # 反向遍历 双指针
        import itertools
        def F(S):
            skip = 0
            for x in reversed(S):
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x

        return all(x == y for x, y in itertools.zip_longest(F(S), F(T)))


import bisect
ls = [1,5,9,13,17]
index1 = bisect.bisect(ls,7)
index2 = bisect.bisect_left(ls,7)
index3 = bisect.bisect_right(ls,7)
print("index1 = {}, index2 = {}, index3 = {}".format(index1, index2, index3))
