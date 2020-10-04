# 输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
# 最大堆(完全二叉树+子节点小于父节点)


def getLeastNumbers(tinput, k):
    # 创建最大堆
    def createMaxHeap(num):
        maxHeap.append(num)
        currentIndex = len(maxHeap) - 1
        while currentIndex != 0:
            parentIndex = (currentIndex - 1) // 2
            if maxHeap[parentIndex] < maxHeap[currentIndex]:
                maxHeap[parentIndex], maxHeap[currentIndex] = maxHeap[currentIndex], maxHeap[parentIndex]
            else:
                break

    # 调整最大堆
    def adjustMaxHeap(num):
        if num < maxHeap[0]:
            maxHeap[0] = num
        maxHeapLen = len(maxHeap)
        index = 0
        while index < maxHeapLen:
            leftIndex = index * 2 + 1
            rightIndex = index * 2 + 2
            if rightIndex < maxHeapLen:
                if maxHeap[rightIndex] < maxHeap[leftIndex]:
                    largerIndex = leftIndex
                else:
                    largerIndex = rightIndex
            elif leftIndex < maxHeapLen:
                largerIndex = leftIndex
            else:
                break
            if maxHeap[index] < maxHeap[largerIndex]:
                maxHeap[index], maxHeap[largerIndex] = maxHeap[largerIndex], maxHeap[index]
            index = largerIndex

    maxHeap = []
    inputLen = len(tinput)
    if len(tinput) < k or k <= 0:
        return []
    for i in range(inputLen):
        if i < k:
            createMaxHeap(tinput[i])
        else:
            adjustMaxHeap(tinput[i])
    return sorted(maxHeap)


if __name__ == '__main__':
    rst = getLeastNumbers([9, 8, 7, 6, 5, 4, 3, 2, 1], 3)
    print(rst)
