# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。


def replaceSpace1(s):
    return s.replace(' ', '%20')


def replaceSpace2(s):
    temp = []
    for i in range(len(s)-1,-1,-1):
        if s[i] == " ":
            temp.append("0")
            temp.append("2")
            temp.append("%")
        else:
            temp.append(s[i])
    temp.reverse()
    return "".join(temp)


if __name__ == '__main__':
    from test.timetest import timetest2

    timetest2(replaceSpace1, replaceSpace2, value="haha haha haha", nums=1, name1='Replace', name2='Implement by self')