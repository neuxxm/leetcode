#11:32AC
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        self.qmin = []
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.q) > 0:
            self.q.append(x)
            t = self.qmin[len(self.qmin)-1]
            if x < t:
                t = x
            self.qmin.append(t)
        else:
            self.q.append(x)
            self.qmin.append(x)
    def pop(self):
        """
        :rtype: None
        """
        if len(self.q) > 0:
            self.q.pop()
            self.qmin.pop()
    def top(self):
        """
        :rtype: int
        """
        if len(self.q) > 0:
            t = self.q[len(self.q)-1]
            return t

    def min(self):
        """
        :rtype: int
        """
        if len(self.q) > 0:
            t = self.qmin[len(self.qmin)-1]
            return t

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()
