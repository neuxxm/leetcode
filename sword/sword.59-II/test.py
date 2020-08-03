#14:03fail
class MaxQueue(object):
    def __init__(self):
        self.q = []
        self.q2 = []

    def max_value(self):
        """
        :rtype: int
        """
        q2 = self.q2
        if q2:
            return q2[0]
        else:
            return -1

    def push_back(self, value):
        """
        :type value: int
        :rtype: None
        """
        q = self.q
        q2 = self.q2
        t = value
        q.append(t)
        while q2:
            if q2[len(q2)-1] < t:
                q2.pop()
            else:
                break
        if q2:
            if t <= q2[0]:
                q2.append(t)
        else:
            q2.append(t)

    def pop_front(self):
        """
        :rtype: int
        """
        q = self.q
        q2 = self.q2
        if q and q2:
            if q[0] == q2[0]:
                t = q.pop(0)
                q2.pop(0)
                return t
            else:
                t = q.pop(0)
                return t
        else:
            return -1
