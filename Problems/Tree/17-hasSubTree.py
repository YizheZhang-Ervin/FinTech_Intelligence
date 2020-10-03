# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def hasSubTree(pRoot1, pRoot2):
    if pRoot2 is None or pRoot1 is None:
        return False

    def hasEqual(pRoot1, pRoot2):
        if pRoot1 is None:
            return False
        if pRoot2 is None:
            return True
        # root
        if pRoot1.val == pRoot2.val:
            # left
            if pRoot2.left is None:
                leftEqual = True
            else:
                leftEqual = hasEqual(pRoot1.left, pRoot2.left)
            # right
            if pRoot2.right is None:
                rightEqual = True
            else:
                rightEqual = hasEqual(pRoot1.right, pRoot2.right)
            return leftEqual and rightEqual
        return False

    # root
    if pRoot1.val == pRoot2.val:
        rst = hasEqual(pRoot1, pRoot2)
        if rst:
            return True
    # left
    rst = hasSubTree(pRoot1.left, pRoot2)
    if rst:
        return True
    # right
    rst = hasSubTree(pRoot1.right, pRoot2)
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
    print(hasSubTree(n1, n5))
