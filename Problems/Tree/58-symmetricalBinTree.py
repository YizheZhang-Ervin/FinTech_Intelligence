# 请实现一个函数，用来判断一棵二叉树是不是对称的。
# 注意，如果一个二叉树同此二叉树的镜像是同样的，定义其为对称的。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetrical(pRoot):
    def isMirror(left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        if left.val != right.val:
            return False
        rst1 = isMirror(left.left, right.right)
        rst2 = isMirror(left.right, right.left)
        return rst1 and rst2
    if pRoot is None:
        return True
    return isMirror(pRoot.left, pRoot.right)


if __name__ == '__main__':
    n1 = TreeNode(2)
    n2 = TreeNode(3)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(5)
    n7 = TreeNode(4)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    print(isSymmetrical(n1))