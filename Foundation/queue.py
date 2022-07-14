"""
补充——关于在 Python 中使用队列
在 Python 中，可以使用以下几种方法实现队列

collections包里的deque，对应操作

pop()从尾取出
appendleft() 从头插入

queue包中的queue，对应操作
put() 插入
get() 取出

直接使用list，只要保证只使用
pop() 取出
insert(0,) 插入
或者只使用
append() 插入
list[0]并且del list[0] 取出

两者使用list方法的不同就区别于你把哪个当头，哪个当尾
三种方法各有优劣。

第一种是正统的Python的双端队列，缺点是调用的函数有点复杂，可能一不小心写了append，就不对了。
第二种使用封装的函数很直接，put()和get()不容易搞混淆。但是queue类型其实里面本身就装了一个deque，有点脱裤子放X的感觉。
第三种优势在于不用调包，但是函数使用逻辑可能造成混淆。在
这里，完整版代码采用第二种，好理解，精简版代码采用第三种，省行数。三种方式可以按照你的喜好互相替换，完全不影响结果。

作者：qsctech-sange
链接：https://leetcode-cn.com/problems/flood-fill/solution/python3-dfs-yu-bfs-liang-chong-fang-fa-san-chong-s/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""