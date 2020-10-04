def sequentialSearch(alist, item):
    """
    未排序的表
    """
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found


def orderedSequentialSearch(alist, item):
    """
    已排序的表
    """
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            # 如果列表中某个值直接大于目标值，因为是有序表，说明后面不会再有相等的了，直接跳查找失败
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found


if __name__ == '__main__':
    # 未排序的列表顺序查找
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))

    # 已排序的列表顺序查找
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(orderedSequentialSearch(testlist, 3))
    print(orderedSequentialSearch(testlist, 13))