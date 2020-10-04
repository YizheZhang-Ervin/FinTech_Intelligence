def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    if first < last:
        # 右指针
        splitpoint = partition(alist, first, last)
        # 根据中值分两半的左半部分递归
        quickSortHelper(alist, first, splitpoint - 1)
        # 根据中值分两半的右半部分递归
        quickSortHelper(alist, splitpoint + 1, last)


# partition另一种方法
# 左指针-1，右指针0
# 左指针-1时，右指针<中值，则左指针、右指针都+1
# 右指针>中值，则右指针+1
# 右指针<中值，则左指针+1的位置与右指针位置的数交换
def partition2(array, first, last):
    i = first - 1
    for j in range(first, last):
        if array[j] < array[last]:
            array[j], array[i + 1] = array[i + 1], array[j]
            i += 1
    array[last], array[i + 1] = array[i + 1], array[last]
    return i + 1


def partition(alist, first, last):
    # 将第一个值设置为中值
    pivotvalue = alist[first]
    # 左指针
    leftmark = first + 1
    # 右指针
    rightmark = last

    done = False
    while not done:
        # 左指针在右指针左边，左指针位置处的值<=中值
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
        # 左指针在右指针左左边，左指针位置处的值>=中值
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
        # 左指针在右指针右边
        if rightmark < leftmark:
            done = True
        # 左指针在右指针左边，左右指针处的值互换
        else:
            alist[leftmark], alist[rightmark] = alist[rightmark], alist[leftmark]
    # 右指针处的值和中值互换
    alist[first], alist[rightmark] = alist[rightmark], alist[first]
    print('当前次序:', alist)
    return rightmark


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quickSort(alist)
    print(alist)
