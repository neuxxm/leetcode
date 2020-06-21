#23:56-0:00
class ListNode:
    def __init__(self, val):
        self.next = None
        self.val = val
class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.a = [None] * 100007

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        t = key%100007
        if self.a[t]:
            p = self.a[t]
            while p:
                if p.val == key:
                    return
                p = p.next
            z = ListNode(key)
            z.next = self.a[t].next
            self.a[t].next = z
        else:
            self.a[t] = ListNode(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        a = self.a
        t = key%100007
        last = None
        p = a[t]
        while p:
            if p.val == key:
                if last:
                    last.next = p.next
                else:
                    a[t] = None
                return
            p = p.next

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        a = self.a
        t = key%100007
        p = a[t]
        while p:
            if p.val == key:
                return True
            p = p.next
        return False
