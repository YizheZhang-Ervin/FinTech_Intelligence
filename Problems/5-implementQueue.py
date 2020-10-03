# 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
# 测试用例:空栈，非空栈


class stackToQueue:
    def __init__(self):
        self.acceptStack = []
        self.outputStack = []

    def push(self, node):
        self.acceptStack.append(node)

    def pop(self):
        if not self.outputStack:
            while self.acceptStack:
                self.outputStack.append(self.acceptStack.pop())

        if self.outputStack:
            return self.outputStack.pop()
        else:
            return None


if __name__ == '__main__':
    stq = stackToQueue()
    stq.push(1)
    stq.push(2)
    stq.push(3)
    r1, r2 = stq.pop(), stq.pop()
    stq.push(4)
    r3, r4 = stq.pop(), stq.pop()
    print(r1, r2, r3, r4)
