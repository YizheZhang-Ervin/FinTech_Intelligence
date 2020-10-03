# 输入一颗二叉树的根节点和一个整数，按字典序打印出二叉树中结点值的和为输入整数的所有路径。路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
import copy


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def findPath(root, expectNumber):
    if root is None:
        return []
    rst = []
    # 保存路径
    supportArrayList = [[root.val]]
    # 广度优先用的node
    support = [root]
    while support:
        tmpNode = support[0]
        tmpArrayList = supportArrayList[0]
        # 判断根结点
        if tmpNode.left is None and tmpNode.right is None:
            if sum(tmpArrayList) == expectNumber:
                rst.insert(0, tmpArrayList)
        if tmpNode.left:
            support.append(tmpNode.left)
            newTmpArrayList = copy.copy(tmpArrayList)
            newTmpArrayList.append(tmpNode.left.val)
            supportArrayList.append(newTmpArrayList)
        if tmpNode.right:
            support.append(tmpNode.right)
            newTmpArrayList = copy.copy(tmpArrayList)
            newTmpArrayList.append(tmpNode.right.val)
            supportArrayList.append(newTmpArrayList)
        del supportArrayList[0]
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
    print(findPath(n1, 7))
