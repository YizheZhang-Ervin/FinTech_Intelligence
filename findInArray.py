# 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
# 请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。


def find1(target, array):
    # O(n^2)
    for i in range(len(array)):
        for j in range(len(array[0])):
            if target == array[i][j]:
                return True
    return False


def find2(target, array):
    # O(m+n)
    row_count, col_count = len(array), len(array[0])
    i, j = 0, col_count-1
    while i < row_count and j >= 0:
        value = array[i][j]
        if value == target:
            return True
        elif value > target:
            j -= 1
        else:
            i += 1
    return False


if __name__ == '__main__':
    from test.timetest import timetest2
    timetest2(find1, find2, value=(5, [[1, 2, 3], [4, 5, 6]]), nums=1, name1='Loop*2', name2='RightTop')