# 从上往下打印出二叉树的每个节点，同层节点从左至右打印。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def printFromTopToBottom(root):
    if root is None:
        return []
    support = [root]
    rst = []
    while support:
        tmpNode = support[0]
        rst.append(tmpNode.val)
        if tmpNode.left:
            support.append(tmpNode.left)
        if tmpNode.right:
            support.append(tmpNode.right)
        del support[0]
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
    print(printFromTopToBottom(n1))