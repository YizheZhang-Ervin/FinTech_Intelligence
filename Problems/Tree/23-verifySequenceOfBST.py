# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。如果是则返回true,否则返回false。假设输入的数组的任意两个数字都互不相同。


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def verifySequenceOfBST(sequence):
    if not sequence:
        return False
    rootNum = sequence[-1]
    del sequence[-1]
    index = None
    for i in range(len(sequence)):
        if index is None and sequence[i] > rootNum:
            index = i
        if index is not None and sequence[i] < rootNum:
            return False
    if not sequence[:index]:
        leftRst = True
    else:
        leftRst = verifySequenceOfBST(sequence[:index])
    if not sequence[index:]:
        rightRst = True
    else:
        rightRst = verifySequenceOfBST(sequence[index:])
    return leftRst and rightRst


if __name__ == '__main__':
    sequence = [1, 4, 2, 6, 3, 9, 5]
    print(verifySequenceOfBST(sequence))