# 操作给定的二叉树，将其变换为源二叉树的镜像。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def mirrorBinTree(root):
    if root is None:
        return None
    # root
    root.left, root.right = root.right, root.left
    # left
    mirrorBinTree(root.left)
    # right
    mirrorBinTree(root.right)
    return root


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
    print(mirrorBinTree(n1).left.val)
