class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # 深度优先遍历:
    # 1.先序(根左右): 12453687
    # 2.中序(左根右): 42516837
    # 3.后序(左右根): 45286731


def preOrderTraverse(root):
    """
        递归形式
    """
    if root is None:
        return
    print(root.val, end=',')
    preOrderTraverse(root.left)
    preOrderTraverse(root.right)


def midOrderTraverse(root):
    """
        递归形式
    """
    if root is None:
        return
    midOrderTraverse(root.left)
    print(root.val, end=',')
    midOrderTraverse(root.right)


def postOrderTraverse(root):
    """
        递归形式
    """
    if root is None:
        return
    postOrderTraverse(root.left)
    postOrderTraverse(root.right)
    print(root.val, end=',')


def preOrderTraverse2(root):
    # 先找到所有左子树，再找每个点右子树
    if root is None:
        return
    stack = []
    tmpNode = root
    while tmpNode or stack:
        while tmpNode:
            print(tmpNode.val, end=',')
            stack.append(tmpNode)
            tmpNode = tmpNode.left
        node = stack.pop()
        tmpNode = node.right


def midOrderTraverse2(root):
    if root is None:
        return
    stack = []
    tmpNode = root
    while tmpNode or stack:
        while tmpNode:
            stack.append(tmpNode)
            tmpNode = tmpNode.left
        node = stack.pop()
        print(node.val, end=',')
        tmpNode = node.right


def postOrderTraverse2(root):
    if root is None:
        return
    stack = []
    tmpNode = root
    while tmpNode or stack:
        while tmpNode:
            stack.append(tmpNode)
            tmpNode = tmpNode.left
        node = stack[-1]
        tmpNode = node.right
        if node.right is None:
            node = stack.pop()
            print(node.val, end=',')
            while stack and node == stack[-1].right:
                node = stack.pop()
                print(node.val, end=',')


if __name__ == '__main__':
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t5 = TreeNode(5)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.left = t6
    t3.right = t7
    t6.right = t8

    preOrderTraverse(t1)
    print("")
    preOrderTraverse2(t1)
    print("")
    midOrderTraverse(t1)
    print("")
    midOrderTraverse2(t1)
    print("")
    postOrderTraverse(t1)
    print("")
    postOrderTraverse2(t1)
