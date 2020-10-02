# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
# 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。


def uglyNumber1(index):
    if index < 1:
        return None
    count = 0

    def isUglyNumber(num):
        while num % 2 == 0:
            num = num // 2
        while num % 3 == 0:
            num = num // 3
        while num % 5 == 0:
            num = num // 5
        if num == 1:
            return True
        return False

    num = 1
    while True:
        if isUglyNumber(num):
            count += 1
        if count == index:
            return num
        num += 1


def uglyNumber2(index):
    if index < 1:
        return 0
    uglyList = [1]
    twoPointer = 0
    threePointer = 0
    fivePointer = 0
    count = 1
    while count != index:
        minValue = min(2*uglyList[twoPointer], 3 * uglyList[threePointer], 5 * uglyList[fivePointer])
        uglyList.append(minValue)
        count += 1
        if minValue == 2*uglyList[twoPointer]:
            twoPointer += 1
        if minValue == 3*uglyList[threePointer]:
            threePointer += 1
        if minValue == 5*uglyList[fivePointer]:
            fivePointer += 1
    return uglyList[count-1]


if __name__ == '__main__':
    print(uglyNumber1(9))
    print(uglyNumber2(9))
