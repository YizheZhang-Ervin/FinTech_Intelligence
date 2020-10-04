# 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
# 注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


def getNext(pNode):
    # 找右子树，存在则找右子树最左
    # 无右子树，找父节点，直到为父节点左子树
    if pNode.right:
        tmpNode = pNode
        while tmpNode.left:
            tmpNode = tmpNode.left
        return tmpNode
    else:
        tmpNode = pNode
        while tmpNode.next:
            if tmpNode.next.left == tmpNode:
                return tmpNode.next
            tmpNode = tmpNode.next
        return None


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
    n2.next = n1
    n4.next = n2
    n5.next = n2
    n3.next = n1
    print(getNext(n5).val)