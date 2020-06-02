class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.q2 = []
        self.tag = 1


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        if self.tag == 1:
            self.q.append(x)
        else:
            self.q2.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.tag == 1:
            while len(self.q) > 1:
                t = self.q.pop(0)
                self.q2.append(t)
            self.tag = 2
            return self.q.pop(0)
        else:
            while len(self.q2) > 1:
                t = self.q2.pop(0)
                self.q.append(t)
            self.tag = 1
            return self.q2.pop(0)


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.tag == 1:
            while len(self.q) > 1:
                t = self.q.pop(0)
                self.q2.append(t)
            t = self.q.pop(0)
            self.q2.append(t)
            self.tag = 2
            return t
        else:
            while len(self.q2) > 1:
                t = self.q2.pop(0)
                self.q.append(t)
            t = self.q2.pop(0)
            self.q.append(t)
            self.tag = 1
            return t


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if self.tag == 1:
            return len(self.q) == 0
        else:
            return len(self.q2) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

