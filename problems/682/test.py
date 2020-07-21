#19:55-20:00
class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        a = ops
        n = len(a)
        q = []
        m = 0
        for i in xrange(n):
            if a[i] == 'C':
                if m > 0:
                    q.pop()
                    m -= 1
            elif a[i] == 'D':
                if m > 0:
                    q.append(q[m-1]*2)
                    m += 1
            elif a[i] == '+':
                if m > 1:
                    q.append(q[m-2]+q[m-1])
                    m += 1
            else:
                q.append(int(a[i]))
                m += 1
        return sum(q)
