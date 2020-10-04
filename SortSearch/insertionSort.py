def insertionSort(alist):
    # 循环逐步扩大有序表
    for index in range(1, len(alist)):
        currentvalue = alist[index]
        position = index
        # 一段范围内，当前值<前面某值(向前对比)，前面最大的某值最终赋给当前值的位置，并逐步扩大有序的范围
        while position > 0 and alist[position - 1] > currentvalue:
            alist[position] = alist[position - 1]
            position = position - 1
        # 最大值赋给当前值位置后，当前值放到最大值的位置
        alist[position] = currentvalue


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertionSort(alist)
    print(alist)