# 把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
# 例如数组[3,4,5,1,2]为[1,2,3,4,5]的一个旋转，该数组的最小值为1。
# NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。


def minNumRotateArray1(rotateArray):
    # O(n)
    import sys
    minNum = sys.maxsize
    for i in range(len(rotateArray)):
        minNum = minNum if minNum < rotateArray[i] else rotateArray[i]
    return minNum


def minNumRotateArray2(rotateArray):
    if not rotateArray: return 0
    left = 0
    right = len(rotateArray) - 1
    while left <= right:
        middle = (left + right) // 2
        if rotateArray[middle - 1] > rotateArray[middle]:
            return rotateArray[middle]
        if rotateArray[middle] > rotateArray[right]:
            left = middle + 1
        elif rotateArray[middle] < rotateArray[right]:
            right = middle - 1
    return 0


if __name__ == '__main__':
    from test.timetest import timetest2

    arr = [3, 4, 5, 1, 2]
    arr2 = [6501, 6828, 6963, 7036, 7422, 7674, 8146, 8468, 8704, 8717, 9170, 9359, 9719, 9895, 9896, 9913, 9962, 154,
            293, 334, 492, 1323, 1479, 1539, 1727, 1870, 1943, 2383, 2392, 2996, 3282, 3812, 3903, 4465, 4605, 4665,
            4772, 4828, 5142, 5437, 5448, 5668, 5706, 5725, 6300, 6335]
    timetest2(minNumRotateArray1, minNumRotateArray2, value=arr2, nums=1, name1='SeqSearch', name2='binsearch')
