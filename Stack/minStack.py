# 155. Min Stack
# 设计一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。

# 实现 MinStack 类:

# MinStack() 初始化堆栈对象。
# void push(int val) 将元素val推入堆栈。
# void pop() 删除堆栈顶部的元素。
# int top() 获取堆栈顶部的元素。
# int getMin() 获取堆栈中的最小元素。

class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or self.min_stack[-1] > val:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

ops  = ["MinStack","push","push","push","getMin","pop","top","getMin","push","push","getMin","pop","getMin"]
args = [[],[-2],[0],[-3],[],[],[],[],[0],[-2],[],[],[]]

obj = None
res = []
for i in range(len(ops)):
    if ops[i] == "MinStack":
        obj = MinStack()
        res.append(None)
    elif ops[i] == "push":
        obj.push(args[i][0])
        res.append(None)
    elif ops[i] == "pop":
        obj.pop()
        res.append(None)
    elif ops[i] == "top":
        res.append(obj.top())
    elif ops[i] == "getMin":
        res.append(obj.getMin())
print(res)  # Output: [null,null,null,null,-3,null,0,-2,null,null,-2,null,-2]