# 从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printBinTreeMultiLine(pRoot):
    if pRoot is None:
        return []
    queue1 = [pRoot]
    queue2 = []
    rst = []
    while queue1 or queue2:
        if queue1:
            tmpRst = []
            while queue1:
                tmpNode = queue1[0]
                tmpRst.append(tmpNode.val)
                del queue1[0]
                if tmpNode.left:
                    queue2.append(tmpNode.left)
                if tmpNode.right:
                    queue2.append(tmpNode.right)
            rst.append(tmpRst)
        if queue2:
            tmpRst = []
            while queue2:
                tmpNode = queue2[0]
                tmpRst.append(tmpNode.val)
                del queue2[0]
                if tmpNode.left:
                    queue1.append(tmpNode.left)
                if tmpNode.right:
                    queue1.append(tmpNode.right)
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
    print(printBinTreeMultiLine(n1))
