# -*- encoding: utf-8 -*-
'''
@File    :   heap.py
@Time    :   2021/11/29 16:47:08
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   堆
heap ref
https://blog.csdn.net/weixin_42377217/article/details/104172668
'''


class heap(list):
    """自定义的堆类型，继承自列表，小顶堆。"""
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.insert(0, len(self))    # 从 1 开始存储，0 标记节点数

    def down_adjust(self, target):
        """调整后使得该位置往下是一个最小堆"""
        child = target * 2
        while child <= self[0]:
            if child +1 <= self[0] and self[child] > self[child+1]:
                child += 1

            if self[child] < self[target]:
                self.swap(child, target)
                target = child
                child = target * 2
            else:
                break

    def up_adjust(self, target):
        while target >= 1:
            parent = target // 2
            if self[parent] > self[target]:
                self.swap(parent, target)
                target = parent
            else:
                break

    def heapify(self):
        """建堆，对有孩子的节点进行向下调整"""
        index = (self[0]) // 2 # 最后一个有孩子的节点索引        
        for i in range(index, 0, -1):
            # import pdb; pdb.set_trace()
            self.down_adjust(i)
    
    def heappop(self):
        """pop 最小节点，向下调整，每次都和最小的孩子交换"""
        if self[0] == 0:
            return None
        result = self[1]
        self[0] -= 1
        if self[0] != 0:
            self[1] = self.pop()    # 将最后一个元素放于堆顶
            self.down_adjust(1)
        return result

    def heappush(self, x):
        # 简单粗暴法，对增加进来的节点进行向上调整
        self[0] += 1
        self.append(x)
        # self.heapify()
        self.up_adjust(self[0])


    def swap(self, i, j):
        self[i], self[j] = self[j], self[i]

    def tolist(self):
        return self[1:]

if __name__ == "__main__":
    import random

    # h = heap([6, 19, 14, 1, 0, 3, 18, 2, 16, 5])
    h = heap([random.randint(0,20) for _ in range(20)])
    print(f'origin nums: {h.tolist()}')
    h.heapify()
    print(f'heapified nums: {h.tolist()}')
    h.heappush(3)
    print(f'push 3, nums: {h.tolist()}')
    
    h.heappop()
    h.heappop()
    h.heappop()
    print(f"pop 3 num, nums: {h.tolist()}")

    nums = [h.heappop() for _ in range(h[0])]
    print(f'heap sort: {nums}')

    
    # nums = [random.randint(0,20) for _ in range(20)]
    # print(f'origin nums: {nums}')
    # sorted_nums = heapsort(nums)
    # print(f'sorted nums: {sorted_nums}')
