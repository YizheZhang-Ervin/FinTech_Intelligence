# 基于插入排序的优化


def shellSort(alist):
    subListCount = 1
    while subListCount < len(alist) / 3:
        subListCount = subListCount * 3 + 1
    # 插排
    while subListCount > 0:
        # 间隔划分为子列表，对每个子列表分别插入排序
        for startPosition in range(subListCount):
            gapInsertionSort(alist, startPosition, subListCount)
        print("After increments of size", subListCount, "The list is", alist)
        subListCount = subListCount // 3


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        # 向前比较
        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shellSort(alist)
    # print(alist)
