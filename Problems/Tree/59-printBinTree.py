# 请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，其他行以此类推。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printBinTree(pRoot):
    if pRoot is None:
        return []
    stack1 = [pRoot]
    stack2 = []
    rst = []
    while stack1 or stack2:
        if stack1:
            tmpRst = []
            while stack1:
                tmpNode = stack1.pop()
                tmpRst.append(tmpNode.val)
                if tmpNode.left:
                    stack2.append(tmpNode.left)
                if tmpNode.right:
                    stack2.append(tmpNode.right)
            rst.append(tmpRst)
        if stack2:
            tmpRst = []
            while stack2:
                tmpNode = stack2.pop()
                tmpRst.append(tmpNode.val)
                if tmpNode.right:
                    stack1.append(tmpNode.right)
                if tmpNode.left:
                    stack1.append(tmpNode.left)
            rst.append(tmpRst)
    return rst


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    print(printBinTree(n1))
