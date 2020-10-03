# 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
# 假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
# 例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def reconstructBinTree(pre, tin):
    if not pre or not tin:
        return None
    if len(pre) != len(tin):
        return None
    root = pre[0]
    rootNode = TreeNode(root)
    pos = tin.index(root)
    tinLeft = tin[:pos]
    tinRight = tin[pos + 1:]
    preLeft = pre[1:pos + 1]
    preRight = pre[pos + 1:]
    leftNode = reconstructBinTree(preLeft, tinLeft)
    rightNode = reconstructBinTree(preRight, tinRight)
    if leftNode:
        rootNode.left = leftNode
    if rightNode:
        rootNode.right = rightNode
    return rootNode


if __name__ == '__main__':
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    print(reconstructBinTree(pre, tin).val)
