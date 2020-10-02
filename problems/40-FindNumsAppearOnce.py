# 一个整型数组里除了两个数字之外，其他的数字都出现了两次。请写程序找出这两个只出现一次的数字。


def FindNumsAppearOnce(array):
    if len(array) < 2:
        return None
    # 整个数组一起异或
    twoNumXor = None
    for num in array:
        if twoNumXor is None:
            twoNumXor = num
        else:
            twoNumXor = twoNumXor ^ num
    # 找出最低位的1
    count = 0
    while twoNumXor % 2 == 0:
        twoNumXor = twoNumXor // 2
        count += 1
    mask = 1 << count
    # 异或结果再循环与数组按位与，分成结果为0和1的两组，每组中得出一个单个的数字
    firstNum, secondNum = None, None
    for num in array:
        if mask & num == 0:
            if firstNum is None:
                firstNum = num
            else:
                firstNum = firstNum ^ num
        else:
            if secondNum is None:
                secondNum = num
            else:
                secondNum = secondNum ^ num
    return firstNum, secondNum


if __name__ == '__main__':
    print(FindNumsAppearOnce([1, 2, 2, 3]))
