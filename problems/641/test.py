#17:16
class MyCircularDeque(object):
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.a = [0] * k
        self.n = k
        self.head = -1
        self.tail = -1
        self.r = False
    def insertFront(self, value):
        """
        Adds an item at the front of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        a = self.a
        n = self.n
        head = self.head
        tail = self.tail
        r = self.r
        print a
        print 'insertFront(%d)'%value, 'h=', head, 't=', tail, 'r=', r
        if self.isEmpty():
            a[0] = value
            self.head += 1
            self.tail += 1
        else:
            if head-1 >= 0:
                if r:
                    if head-1>tail:
                        a[head-1] = value
                        self.head -= 1
                    else:
                        return False
                else:
                    a[head-1] = value
                    self.head -= 1
            else:
                t = head-1+n
                if tail < t:
                    a[t] = value
                    self.head = t
                    self.r = True
                else:
                    return False
        return True
    def insertLast(self, value):
        """
        Adds an item at the rear of Deque. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        a = self.a
        n = self.n
        head = self.head
        tail = self.tail
        r = self.r
        print a
        print 'insertFront(%d)'%value, 'h=', head, 't=', tail
        if self.isEmpty():
            a[0] = value
            self.head += 1
            self.tail += 1
        else:
            if tail+1 < n:
                if r:
                    if tail+1 < head:
                        a[tail+1] = value
                        self.tail += 1
                    else:
                        return False
                else:
                    a[tail+1] = value
                    self.tail += 1
            else:
                t = (tail+1)%n
                if t < head:
                    a[t] = value
                    self.tail = t
                    self.r = True
                else:
                    return False
        return True
    def deleteFront(self):
        """
        Deletes an item from the front of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.head += 1
        if self.head == n:
            self.head = 0
            self.r = False
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            self.r = False
        return True
    def deleteLast(self):
        """
        Deletes an item from the rear of Deque. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.tail -= 1
        if self.tail == -1:
            self.tail = n-1
            self.r = False
        if self.tail == self.head:
            self.head = -1
            self.tail = -1
            self.r = False
        return True
    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            #print 'getGear', self.a[self.head]
            return self.a[self.head]
    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            #print 'getGear', self.a[self.tail]
            return self.a[self.tail]
    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        return self.head == self.tail and self.head == -1
    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        #print 'isFull'
        if self.r:
            return self.tail + 1 == self.head
        else:
            return self.tail == self.n-1 and self.head == 0
m = MyCircularDeque(3)
m.insertLast(1)
m.insertLast(2)
m.insertFront(3)
m.insertFront(4)
