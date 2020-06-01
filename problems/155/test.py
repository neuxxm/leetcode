#20:10
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []
        self.q2 = []


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
		q.append(x)
        if len(q2) > 0:
            mi = q2.top()
            if x < mi:
                mi = x
            q2.append(mi)
        else:
		    q2.append(x)


    def pop(self):
        """
        :rtype: None
        """
        q.pop()
        q2.pop()

    def top(self):
        """
        :rtype: int
        """
        return q[0]


    def getMin(self):
        """
        :rtype: int
        """
        return q2[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
