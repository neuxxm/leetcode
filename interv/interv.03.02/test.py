#11:12-11:24
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
        q = self.q
        q2 = self.q2
        q.append(x)
        if len(q2) == 0:
            q2.append(x)
        else:
            mi = q2[len(q2)-1]
            if x < mi:
                mi = x
            q2.append(mi)

    def pop(self):
        """
        :rtype: None
        """
        q = self.q
        q2 = self.q2
        if len(q) == 0:
            return
        q.pop()
        q2.pop()

    def top(self):
        """
        :rtype: int
        """
        q = self.q
        if len(q) > 0:
            return q[len(q)-1]

    def getMin(self):
        """
        :rtype: int
        """
        q2 = self.q2
        if len(q2) > 0:
            return q2[len(q2)-1]
