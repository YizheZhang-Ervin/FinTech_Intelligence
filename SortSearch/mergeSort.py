# 分治法，不断拆一半，然后拉对比链合并
# Map(mergeSort) + Reduce(mergeCore)


def mergeSort(alist):
    print("Splitting ", alist)
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
    # 右表比完之后，左表还有遗留，逐个加入总表(用extend和while等效)
    # rst.extend(leftList[leftIndex:])
    while leftIndex < leftLen:
        rst.append(leftList[leftIndex])
        leftIndex += 1
    # 左表比完之后，右表还有遗留，逐个加入总表(用extend和while等效)
    # rst.extend(rightList[rightIndex:])
    while rightIndex < rightLen:
        rst.append(rightList[rightIndex])
        rightIndex += 1
    print("Merging ", rst)
    return rst


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort(alist)
