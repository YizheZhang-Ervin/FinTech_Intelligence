# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。


class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n


def entryNodeOfLoop(pHead):
    # 两个指针:快(2步)、慢(1步)
    if pHead is None:
        return None
    fastPointer = pHead
    slowPointer = pHead
    while fastPointer and fastPointer.next:
        fastPointer = fastPointer.next.next
        slowPointer = slowPointer.next
        if fastPointer == slowPointer:
            break
    if fastPointer.next is None or slowPointer.next is None:
        return None
    # 找入口点
    newPointer = pHead
    while newPointer != slowPointer:
        newPointer = newPointer.next
        slowPointer = slowPointer.next
    return newPointer


if __name__ == '__main__':
    n6 = ListNode(2, None)
    n5 = ListNode(2, n6)
    n4 = ListNode(2, n5)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    n6.next = n3
    print(entryNodeOfLoop(n1).val)
