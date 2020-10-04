# 如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
# 如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
# 我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。


class DataFlow:
    def __init__(self):
        self.littleValueMaxHeap = []
        self.bigValueMinHeap = []
        self.maxHeapCount = 0
        self.minHeapCount = 0

    def createMaxHeap(self, num):
        self.littleValueMaxHeap.append(num)
        tmpIndex = len(self.littleValueMaxHeap) - 1
        while tmpIndex:
            parentIndex = (tmpIndex - 1) // 2
            if self.littleValueMaxHeap[parentIndex] < self.littleValueMaxHeap[tmpIndex]:
                self.littleValueMaxHeap[parentIndex], self.littleValueMaxHeap[tmpIndex] = \
                    self.littleValueMaxHeap[tmpIndex], self.littleValueMaxHeap[parentIndex]
                tmpIndex = parentIndex
            else:
                break

    def adjustMaxHeap(self, num):
        if num < self.littleValueMaxHeap[0]:
            maxHeapLen = len(self.littleValueMaxHeap)
            self.littleValueMaxHeap[0] = num
            tmpIndex = 0
            while tmpIndex < maxHeapLen:
                leftIndex = tmpIndex * 2 + 1
                rightIndex = tmpIndex * 2 + 2
                if rightIndex < maxHeapLen:
                    largerIndex = rightIndex \
                        if self.littleValueMaxHeap[leftIndex] < self.littleValueMaxHeap[rightIndex] else leftIndex
                elif leftIndex < maxHeapLen:
                    largerIndex = leftIndex
                else:
                    break
                if self.littleValueMaxHeap[tmpIndex] < self.littleValueMaxHeap[largerIndex]:
                    self.littleValueMaxHeap[tmpIndex], self.littleValueMaxHeap[largerIndex] = \
                        self.littleValueMaxHeap[largerIndex], self.littleValueMaxHeap[tmpIndex]
                    tmpIndex = largerIndex
                else:
                    break

    def createMinHeap(self, num):
        self.bigValueMinHeap.append(num)
        tmpIndex = len(self.bigValueMinHeap) - 1
        while tmpIndex:
            parentIndex = (tmpIndex - 1) // 2
            if self.bigValueMinHeap[tmpIndex] < self.bigValueMinHeap[parentIndex]:
                self.bigValueMinHeap[parentIndex], self.bigValueMinHeap[tmpIndex] = \
                    self.bigValueMinHeap[tmpIndex], self.bigValueMinHeap[parentIndex]
                tmpIndex = parentIndex
            else:
                break

    def adjustMinHeap(self, num):
        if num < self.bigValueMinHeap[0]:
            minHeapLen = len(self.bigValueMinHeap)
            self.bigValueMinHeap[0] = num
            tmpIndex = 0
            while tmpIndex < minHeapLen:
                leftIndex = tmpIndex * 2 + 1
                rightIndex = tmpIndex * 2 + 2
                if rightIndex < minHeapLen:
                    smallerIndex = rightIndex if self.bigValueMinHeap[rightIndex] < self.bigValueMinHeap[
                        leftIndex] else leftIndex
                elif leftIndex < minHeapLen:
                    smallerIndex = leftIndex
                else:
                    break
                if self.bigValueMinHeap[smallerIndex] < self.bigValueMinHeap[tmpIndex]:
                    self.bigValueMinHeap[tmpIndex], self.bigValueMinHeap[smallerIndex] = \
                        self.bigValueMinHeap[smallerIndex], self.bigValueMinHeap[tmpIndex]
                    tmpIndex = smallerIndex
                else:
                    break

    def Insert(self, num):
        if self.maxHeapCount > self.minHeapCount:
            self.minHeapCount += 1
            if num < self.littleValueMaxHeap[0]:
                tmpNum = self.littleValueMaxHeap[0]
                self.adjustMaxHeap(num)
                self.createMinHeap(tmpNum)
            else:
                self.createMinHeap(num)
        else:
            self.maxHeapCount += 1
            if len(self.littleValueMaxHeap) == 0:
                self.createMaxHeap(num)
            else:
                if self.bigValueMinHeap[0] < num:
                    tmpNum = self.bigValueMinHeap[0]
                    self.adjustMinHeap(num)
                    self.createMaxHeap(tmpNum)
                else:
                    self.createMaxHeap(num)

    def getMedian(self):
        if self.minHeapCount < self.maxHeapCount:
            return self.littleValueMaxHeap[0]
        else:
            return float((self.littleValueMaxHeap[0] + self.bigValueMinHeap[0]) / 2)


if __name__ == '__main__':
    df = DataFlow()
    arr = [5, 2, 3, 4, 1, 6, 7, 0, 8]
    arr2 = [9, 3, 15, 14, 6, 7, 22, 5, 20]
    for i in arr:
        df.Insert(i)
        print(df.getMedian())
