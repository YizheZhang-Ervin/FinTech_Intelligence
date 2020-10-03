# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。


def add(num1, num2):
    xorNum = num1 ^ num2
    andNum = (num1 & num2) << 1
    while andNum != 0:
        tmp1 = xorNum ^ andNum
        tmp2 = (xorNum & andNum) << 1
        tmp1 = tmp1 & 0xFFFFFFFF
        xorNum = tmp1
        andNum = tmp2

    return xorNum if xorNum <= 0x7FFFFFFF else ~(xorNum ^ 0xFFFFFFFF)


if __name__ == '__main__':
    print(add(-2, -8))
    print(add(10, 8))
