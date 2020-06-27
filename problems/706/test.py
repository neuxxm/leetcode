#11:59-12:04
class ListNode:
    def __init__(self, val):
        self.val = val
class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.m = 100007
        self.a = [None] * self.m

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: None
        """
        h = key%self.m
        a = self.a
        if a[h]:
            a[h].val = value
        else:
            a[h] = ListNode(value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        h = key%self.m
        a = self.a
        if a[h]:
            return a[h].val
        else:
            return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: None
        """
        h = key%self.m
        a = self.a
        if a[h]:
            a[h] = None
