#13:40-13:44
class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.q2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.q.append(x)


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        q = self.q
        q2 = self.q2
        while q:
            q2.append(q.pop())
        t = q2.pop()
        while q2:
            q.append(q2.pop())
        return t

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        q = self.q
        q2 = self.q2
        while q:
            q2.append(q.pop())
        t = q2[len(q2)-1]
        while q2:
            q.append(q2.pop())
        return t

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.q) == 0
