# 请实现两个函数，分别用来序列化和反序列化二叉树
# 二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。
# 序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。
# 二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。
# 例如，我们可以把一个只有根节点为1的二叉树序列化为"1,"，然后通过自己的函数来解析回这个二叉树


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def serialize(root):
    rstList = []

    def preOrder(root):
        if root is None:
            rstList.append('#')
            return
        rstList.append(str(root.val))
        preOrder(root.left)
        preOrder(root.right)
    preOrder(root)
    return " ".join(rstList)


def deserialize(s):
    rstList = s.split()

    def dePreOrder():
        if not rstList:
            return None
        rootVal = rstList[0]
        del rstList[0]
        if rootVal == '#':
            return None
        node = TreeNode(int(rootVal))
        leftNode = dePreOrder()
        rightNode = dePreOrder()
        node.left = leftNode
        node.right = rightNode
        return node
    pRoot = dePreOrder()
    return pRoot


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
    rst = serialize(n1)
    print(rst)
    print(deserialize(rst).val)