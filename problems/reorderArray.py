# 输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。


def reorderArray1(array):
    # Time: O(n), Space: O(n)
    rst = []
    for i in array:
        if i % 2 != 0:
            rst.append(i)
    for j in array:
        if j % 2 == 0:
            rst.append(j)
    return rst


def reorderArray2(array):
    odd_index = -1
    for i, v in enumerate(array):
        if v % 2 != 0:
            if i - odd_index == 1:
                odd_index = i
            else:
                current_value = v
                for j in range(i, odd_index+1, -1):
                    array[j] = array[j - 1]
                array[odd_index+1] = current_value
                odd_index += 1
    return array


if __name__ == '__main__':
    from test.timetest import timetest2

    arr = [1, 3,2,4,5]
    timetest2(reorderArray1, reorderArray2, value=arr, nums=1, name1='ExtraSpace', name2='ExtraTime')
