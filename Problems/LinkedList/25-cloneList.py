# 输入一个复杂链表（每个节点中有节点值，以及两个指针，一个指向下一个节点，另一个特殊指针random指向一个随机节点），
# 请对此链表进行深拷贝，并返回拷贝后的头结点。（注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）


class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


def cloneList1(pHead):
    import copy
    rst = copy.deepcopy(pHead)
    return rst


def cloneList2(pHead):
    if pHead is None:
        return None
    # 复制node并加到链表每个node后
    pTmp = pHead
    while pTmp:
        node = RandomListNode(pTmp.label)
        node.next = pTmp.next
        pTmp.next = node
        pTmp = node.next
    # 实现新node的random指向
    pTmp = pHead
    while pTmp:
        if pTmp.random:
            pTmp.next.random = pTmp.random.next
        pTmp = pTmp.next.next
    # 断开原node于新node的链接
    pTmp = pHead
    newHead = pHead.next
    pNewTmp = pHead.next
    while pTmp:
        pTmp.next = pTmp.next.next
        if pNewTmp.next:
            pNewTmp.next = pNewTmp.next.next
            pNewTmp = pNewTmp.next
        pTmp = pTmp.next
    return newHead


if __name__ == '__main__':
    n3 = RandomListNode(3)
    n2 = RandomListNode(2)
    n1 = RandomListNode(1)
    n3.next = None
    n3.random = n1
    n2.next = n3
    n2.random = n2
    n1.next = n2
    n1.random = n3
    print(cloneList1(n1).label)
    print(cloneList2(n1).label)