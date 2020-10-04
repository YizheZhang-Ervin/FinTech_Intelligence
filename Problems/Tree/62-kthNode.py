# 给定一棵二叉搜索树，请找出其中的第k小的结点。
# 例如， （5，3，7，2，4，6，8）中，按结点数值大小顺序第三小结点的值为4。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def kthNode(pRoot, k):
    rstList = []

    def preOrder(pRoot):
        if pRoot is None:
            return None
        preOrder(pRoot.left)
        rstList.append(pRoot.val)
        preOrder(pRoot.right)

    preOrder(pRoot)
    if len(rstList) < k or k < 1:
        return None
    return rstList[k - 1]


if __name__ == '__main__':
    n1 = TreeNode(5)
    n2 = TreeNode(3)
    n3 = TreeNode(7)
    n4 = TreeNode(2)
    n5 = TreeNode(4)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    print(kthNode(n1,3))
