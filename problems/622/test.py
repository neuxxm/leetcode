#20:02AC
class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.a = [0] * k
        self.size = k
        self.head = 0
        self.tail = 0
        self.cnt = 0

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.cnt == self.size:
            return False
        if self.tail < self.size:
            self.a[self.tail] = value
            self.tail += 1
            self.cnt += 1
            if self.tail == self.size:
                self.tail = 0
            return True
           
    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.cnt == 0:
            return False
        if self.head < self.size:
            self.head += 1
            self.cnt -= 1
            if self.head == self.size:
                self.head = 0
            return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.a[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.a[self.tail-1]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.cnt == 0
        
    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.cnt == self.size
