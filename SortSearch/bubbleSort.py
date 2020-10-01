def bubbleSort(array):
    # 将大的后置
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


if __name__ == '__main__':
    arr = [9, 3, 4, 5, 2, 1, 6, 8, 7]
    rst = bubbleSort(arr)
    print(rst)
