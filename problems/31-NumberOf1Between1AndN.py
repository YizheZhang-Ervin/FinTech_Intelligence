# 求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
# 为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
# ACMer希望你们帮帮他,并把问题更加普遍化,可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。


def numOf1Between1AndN(n):
    precise = 1
    highValue = 1
    midValue = 1
    lowValue = 1
    count = 0
    sumNum = 0
    while highValue != 0:
        highValue = n // (precise * 10)
        midValue = (n // precise) % 10
        lowValue = n % precise
        precise = precise * 10
        if midValue == 0:
            num = (highValue - 1 + 1) * pow(10, count)
        elif midValue > 1:
            num = (highValue + 1) * pow(10, count)
        else:
            num = highValue * pow(10, count) + lowValue+1
        sumNum += num
        count += 1
    return sumNum


if __name__ == '__main__':
    print(numOf1Between1AndN(10))
