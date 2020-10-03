# 输入一个链表，按链表从尾到头的顺序返回一个ArrayList。


class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n


def printListTailToHead(listNode):
    rst = []
    pTmp = listNode
    while pTmp:
        rst.insert(0, pTmp.val)
        pTmp = pTmp.next
    return rst


if __name__ == '__main__':
    n3 = ListNode(3, None)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    print(printListTailToHead(n1))
