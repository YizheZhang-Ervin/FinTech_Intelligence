# 数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
# 例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
# 由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。


def moreThanHalfNumber1(numbers):
    numsCount = {}
    numLen = len(numbers)
    for num in numbers:
        if num in numsCount:
            numsCount[num] += 1
        else:
            numsCount[num] = 1
        if numsCount[num] > numLen // 2:
            return num
    return 0


def moreThanHalfNumber2(numbers):
    last = 0
    lastCount = 0
    for num in numbers:
        if lastCount == 0:
            last = num
            lastCount = 1
        else:
            if num == last:
                lastCount += 1
            else:
                lastCount -= 1
    if lastCount == 0:
        return 0
    else:
        lastCount = 0
        for num in numbers:
            if num == last:
                lastCount += 1
        if lastCount > len(numbers)//2:
            return last
    return 0


if __name__ == '__main__':
    print(moreThanHalfNumber1([1, 2, 3, 4, 5, 2, 2, 2, 2]))
    print(moreThanHalfNumber2([1, 2, 3, 4, 5, 2, 2, 2, 2]))
