#15:42-15:50
class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        m = n
        a = target
        n = len(a)
        r = []
        last = 0
        for i in xrange(0, n):
            if i == 0:
                if a[i] == 1:
                    r.append('Push')
                else:
                    for k in xrange(1, a[i]):
                        r.append('Push')
                        r.append('Pop')
                    r.append('Push')
            elif a[i]-1 == i:
                r.append('Push')
            else:
                for k in xrange(a[i-1]+1, a[i]):
                    r.append('Push')
                    r.append('Pop')
                r.append('Push')
        return r
