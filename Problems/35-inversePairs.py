# 在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
# 输入一个数组,求出这个数组中的逆序对的总数P。
# 并将P对1000000007取模的结果输出。 即输出P%1000000007


def inversePairs(data):
    global count
    count = 0

    def mergeSort(alist):
        lens = len(alist)
        if lens < 1:
            return []
        if lens == 1:
            return alist
        if lens > 1:
            # 拆分左半右半
            mid = lens // 2
            lefthalf = alist[:mid]
            righthalf = alist[mid:]
            # 递归归并排序
            sortedLeft = mergeSort(lefthalf)
            sortedRight = mergeSort(righthalf)
            return mergeCore(sortedLeft, sortedRight)

    def mergeCore(leftList, rightList):
        leftIndex, rightIndex, leftLen, rightLen = 0, 0, len(leftList), len(rightList)
        rst = []
        global count
        # 拉链对比
        while leftIndex < leftLen and rightIndex < rightLen:
            # 左小，左数加入总表
            if leftList[leftIndex] < rightList[rightIndex]:
                rst.append(leftList[leftIndex])
                leftIndex += 1
            # 右小，右数加入总表
            else:
                rst.append(rightList[rightIndex])
                rightIndex += 1
                # 移动的位数即为逆序对的个数
                count += leftLen-rightIndex+1
        # 右表比完之后，左表还有遗留，逐个加入总表(用extend和while等效)
        rst.extend(leftList[leftIndex:])
        # 左表比完之后，右表还有遗留，逐个加入总表(用extend和while等效)
        rst.extend(rightList[rightIndex:])
        return rst
    return mergeSort(data), count


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 0]
    rsts = inversePairs(arr)[1]
    print(rsts)
