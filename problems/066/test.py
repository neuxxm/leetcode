#20:20-20:23
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        a = digits
        tag = 1
        n = len(a)
        for i in xrange(n-1, -1, -1):
            t = a[i] + tag
            if t >= 10:
                t -= 10
                tag = 1
            else:
                tag = 0
            a[i] = t
        if tag > 0:
            a.append(0)
            for i in xrange(n, 0, -1):
                a[i] = a[i-1]
            a[0] = tag
        return a
