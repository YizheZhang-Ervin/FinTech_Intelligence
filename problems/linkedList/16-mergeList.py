# 输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。


class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n


def mergeList(pHead1, pHead2):
    if pHead1 is None:
        return pHead2
    if pHead2 is None:
        return pHead1
    newHead = pHead1 if pHead1.val < pHead2.val else pHead2
    pTmp = pHead1
    pTmp2 = pHead2
    if newHead == pTmp:
        pTmp = pTmp.next
    else:
        pTmp2 = pTmp2.next
    previousPointer = newHead
    while pTmp and pTmp2:
        if pTmp.val < pTmp2.val:
            previousPointer.next = pTmp
            previousPointer = pTmp
            pTmp = pTmp.next
        else:
            previousPointer.next = pTmp2
            previousPointer = pTmp2
            pTmp2 = pTmp2.next
    if not pTmp:
        previousPointer.next = pTmp2
    else:
        previousPointer.next = pTmp
    return newHead


if __name__ == '__main__':
    n3 = ListNode(3, None)
    n2 = ListNode(2, n3)
    n1 = ListNode(1, n2)
    print(mergeList(n1).val)
