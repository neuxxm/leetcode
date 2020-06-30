#11:15-11:18
class CQueue(object):

    def __init__(self):
        self.q = []
        self.q2 = []

    def appendTail(self, value):
        """
        :type value: int
        :rtype: None
        """
        q = self.q
        q.append(value)


    def deleteHead(self):
        """
        :rtype: int
        """
        q = self.q
        q2 = self.q2
        if len(q) > 0:
            while len(q) > 1:
                t = q.pop()
                q2.append(t)
            r = q.pop()
            while len(q2) > 0:
                q.append(q2.pop())
            return r
        else:
            return -1
