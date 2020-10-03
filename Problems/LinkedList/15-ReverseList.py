# 输入一个链表，反转链表后，输出新链表的表头。


class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n


def reverseList(pHead):
    if pHead is None:
        return None
    if pHead.next is None:
        return pHead

    leftPointer = pHead
    midPointer = pHead.next
    rightPointer = pHead.next.next
    leftPointer.next = None

    while rightPointer is not None:
        midPointer.next = leftPointer
        leftPointer = midPointer
        midPointer = rightPointer
        rightPointer = rightPointer.next
    midPointer.next = leftPointer
    return midPointer


if __name__ == '__main__':
    n3 = ListNode(3, None)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    print(reverseList(n1).val)
