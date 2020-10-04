# 封装版


class DataFlow:
    def __init__(self):
        self.littleValueMaxHeap = []
        self.bigValueMinHeap = []
        self.maxHeapCount = 0
        self.minHeapCount = 0

    def Insert(self, num):
        def cmpMaxHeap(a, b):
            return a > b

        def cmpMinHeap(a, b):
            return a < b

        if self.maxHeapCount > self.minHeapCount:
            self.minHeapCount += 1
            if num < self.littleValueMaxHeap[0]:
                tmpNum = self.littleValueMaxHeap[0]
                self.adjustHeap(num, self.littleValueMaxHeap,cmpMaxHeap)
                self.createHeap(tmpNum, self.bigValueMinHeap, cmpMinHeap)
            else:
                self.createHeap(num, self.bigValueMinHeap, cmpMinHeap)
        else:
            self.maxHeapCount += 1
            if len(self.littleValueMaxHeap) == 0:
                self.createHeap(num, self.littleValueMaxHeap, cmpMaxHeap)
            else:
                if self.bigValueMinHeap[0] < num:
                    tmpNum = self.bigValueMinHeap[0]
                    self.adjustHeap(num, self.bigValueMinHeap,cmpMinHeap)
                    self.createHeap(tmpNum, self.littleValueMaxHeap, cmpMaxHeap)
                else:
                    self.createHeap(num, self.littleValueMaxHeap, cmpMaxHeap)

    def getMedian(self):
        if self.minHeapCount < self.maxHeapCount:
            return self.littleValueMaxHeap[0]
        else:
            return float((self.littleValueMaxHeap[0] + self.bigValueMinHeap[0]) / 2)

    def createHeap(self, num, heap, cmpFunc):
        heap.append(num)
        tmpIndex = len(heap) - 1
        while tmpIndex:
            parentIndex = (tmpIndex - 1) // 2
            if cmpFunc(heap[tmpIndex], heap[parentIndex]):
                heap[parentIndex], heap[tmpIndex] = heap[tmpIndex], heap[parentIndex]
                tmpIndex = parentIndex
            else:
                break

    def adjustHeap(self, num, heap, cmpFunc):
        if num < heap[0]:
            heapLen = len(heap)
            heap[0] = num
            tmpIndex = 0
            while tmpIndex < heapLen:
                leftIndex = tmpIndex * 2 + 1
                rightIndex = tmpIndex * 2 + 2
                if rightIndex < heapLen:
                    xIndex = rightIndex if cmpFunc(heap[rightIndex], heap[leftIndex]) else leftIndex
                elif leftIndex < heapLen:
                    xIndex = leftIndex
                else:
                    break
                if cmpFunc(heap[xIndex], heap[tmpIndex]):
                    heap[tmpIndex], heap[xIndex] = heap[xIndex], heap[tmpIndex]
                    tmpIndex = xIndex
                else:
                    break


if __name__ == '__main__':
    df = DataFlow()
    arr = [5, 2, 3, 4, 1, 6, 7, 0, 8]
    arr2 = [9, 3, 15, 14, 6, 7, 22, 5, 20]
    for i in arr:
        df.Insert(i)
        print(df.getMedian())