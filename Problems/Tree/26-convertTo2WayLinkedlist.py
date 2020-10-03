# 输入一棵二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def convert(pRootOfTree):
    if pRootOfTree is None:
        return None

    # 找右结点
    def find_right(node):
        while node.right:
            node = node.right
        return node

    leftNode = convert(pRootOfTree.left)
    rightNode = convert(pRootOfTree.right)
    rstNode = leftNode

    if leftNode:
        leftNode = find_right(leftNode)
    else:
        rstNode = pRootOfTree
    pRootOfTree.left = leftNode
    pRootOfTree.right = rightNode
    if leftNode is not None:
        leftNode.right = pRootOfTree
    if rightNode is not None:
        rightNode.left = pRootOfTree
    return rstNode


if __name__ == '__main__':
    n1 = TreeNode(5)
    n2 = TreeNode(2)
    n3 = TreeNode(9)
    n4 = TreeNode(1)
    n5 = TreeNode(3)
    n6 = TreeNode(6)
    n7 = TreeNode(11)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    head = convert(n1)
    for i in range(7):
        print(head.val,end=',')
        head = head.right
