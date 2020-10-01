# 输入一个链表，输出该链表中倒数第k个结点。


class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n


def FindKthToTail(head, k):
    firstPoint = head
    secondPoint = head
    for i in range(k):
        if firstPoint is None:
            return None
        firstPoint = firstPoint.next
    while firstPoint is not None:
        firstPoint = firstPoint.next
        secondPoint = secondPoint.next
    return secondPoint


if __name__ == '__main__':
    n3 = ListNode(3, None)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    print(FindKthToTail(n1, 2).val)
