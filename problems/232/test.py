#13:01AC
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.q2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        q = self.q
        q.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        q = self.q
        q2 = self.q2
        while len(q) > 1:
            q2.append(q.pop())
        t = q.pop()
        while len(q2) > 0:
            q.append(q2.pop())
        return t

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        q = self.q
        q2 = self.q2
        while len(q) > 1:
            q2.append(q.pop())
        t = q[0]
        while len(q2) > 0:
            q.append(q2.pop())
        return t

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return len(self.q) == 0
