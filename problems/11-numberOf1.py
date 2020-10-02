# 输入一个整数，输出该数32位二进制表示中1的个数。其中负数用补码表示。


def numberOfOne(n):
    count = 0
    # 与运算得到补码
    for c in str(bin(n & 0xffffffff))[2:]:
        if c == '1':
            count += 1
    return count


def numberOfOne2(n):
    count = 0
    for i in range(32):
        mask = 1 << i
        if n & mask != 0:
            count += 1
    return count


def numberOfOne3(n):
    count = 0
    while n:
        n = n & (n-1)
        count += 1
        n = 0xFFFFFFFF & n
    return count


if __name__ == '__main__':
    rst1 = numberOfOne(-10)
    rst2 = numberOfOne2(-10)
    rst3 = numberOfOne3(-10)
    print(rst1, rst2, rst3)
