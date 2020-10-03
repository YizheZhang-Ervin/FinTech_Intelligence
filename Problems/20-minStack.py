# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。


class minStack:
    def __init__(self):
        self.stack = []
        self.minValue = []

    def push(self, node):
        self.stack.append(node)
        if self.minValue:
            if self.minValue[-1] > node:
                self.minValue.append(node)
            else:
                self.minValue.append(self.minValue[-1])
        else:
            self.minValue.append(node)

    def pop(self):
        if not self.stack:
            return None
        self.minValue.pop()
        self.stack.pop()

    def top(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def min(self):
        if not self.minValue:
            return None
        return self.minValue[-1]


if __name__ == '__main__':
    ms = minStack()
    ms.push(7), ms.push(3), ms.push(2), ms.push(8), ms.push(1)
    rst1 = ms.min()
    ms.pop()
    rst2 = ms.min()
    print(rst1, rst2)
