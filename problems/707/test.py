#16:42AC
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.h = ListNode(0)
    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        h = self.h
        p = h.next
        ix = 0
        while p:
            if ix == index:
                return p.val
            p = p.next
            ix += 1
        return -1
    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        h = self.h
        t = ListNode(val)
        t.next = h.next
        h.next = t
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        h = self.h
        p = h.next
        while p.next:
            p = p.next
        p.next = ListNode(val)
    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        h = self.h
        if index == 0:
            t = ListNode(val)
            t.next = h.next
            h.next = t
            return
        p = h.next
        ix = 0
        while p:
            if ix == index-1:
                break
            p = p.next
            ix += 1
        if ix != index-1:
            return
        t = ListNode(val)
        t.next = p.next
        p.next = t
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        h = self.h
        p = h.next
        ix = 0
        last = h
        while p:
            if ix == index:
                break
            last = p
            p = p.next
            ix += 1
        if ix != index:
            return
        if last.next == None:
            return
        last.next = last.next.next
