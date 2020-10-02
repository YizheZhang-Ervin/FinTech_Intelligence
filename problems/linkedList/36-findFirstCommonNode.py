# 输入两个链表，找出它们的第一个公共结点。（注意因为传入数据是链表，所以错误测试数据的提示是用其他方式显示的，保证传入数据是正确的）


class ListNode:
    def __init__(self, x, n):
        self.val = x
        self.next = n


def findFirstCommonNode(pHead1, pHead2):
    pTmp1 = pHead1
    pTmp2 = pHead2
    while pTmp1 and pTmp2:
        # 两链表一样长
        if pTmp1 == pTmp2:
            return pTmp1
        pTmp1 = pTmp1.next
        pTmp2 = pTmp2.next

    def findEqual(shortPointer, longPointer, shortHead, longHead):
        k = 0
        # 链表长度差值
        while longPointer:
            longPointer = longPointer.next
            k += 1
        # 长链表先走k步
        shortPointer = shortHead
        longPointer = longHead
        for i in range(k):
            longPointer = longPointer.next
        while longPointer != shortPointer:
            longPointer = longPointer.next
            shortPointer = shortPointer.next
        return longPointer

    if pTmp1:
        return findEqual(pTmp2, pTmp1, pHead2, pHead1)
    if pTmp2:
        return findEqual(pTmp1, pTmp2, pHead1, pHead2)


if __name__ == '__main__':
    n4 = ListNode(4, None)
    n3 = ListNode(3, n4)
    n2 = ListNode(2, n4)
    n1 = ListNode(1, n2)
    print(findFirstCommonNode(n1, n3).val)
