# jumpfloor: 一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
# jumpfloor2: 一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。


def jumpfloor(number):
    if number < 1:
        return 0
    if number == 1:
        return 1
    if number == 2:
        return 2
    n1, n2 = 1, 2
    rst = 0
    for i in range(3, number + 1):
        rst = n1 + n2
        n1, n2 = n2, rst
    return rst


def jumpfloor2(number):
    # method1
    n1 = 1
    rst = 1
    if number == 1:
        return 1
    for i in range(2, number+1):
        rst = 2*n1
        n1 = rst
    return rst
    # method2: return pow(2,number-1)


if __name__ == '__main__':
    from test.timetest import timetest1
    timetest1(jumpfloor, value=30, nums=2, name1='Jumpfloor1')
    timetest1(jumpfloor2, value=30, nums=2, name1='Jumpfloor2')