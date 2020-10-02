# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。n<=39
# 测试用例: 负数、0、1、2~39


# 循环
def fib1(n):
    n0 = 0
    n1 = 1
    num = 0
    if n == 0:
        return n0
    if n == 1:
        return n1
    if n > 1:
        for i in range(2, n + 1):
            num = n0 + n1
            n1, n0 = num, n1
        return num
    return None


# 递归-时间复杂度过大2^n
def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n > 1:
        return fib2(n - 1) + fib2(n - 2)
    return None


if __name__ == '__main__':
    from test.timetest import timetest1, timetest2

    timetest2(fib1, fib2, value=30, nums=2, name1='Loop', name2='Recursion')
    timetest1(fib1, value=30, nums=2, name1='Loop')
