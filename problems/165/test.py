#20:16-20:24
def f(s):
    s = s.lstrip('0')
    if s == '':
        s = '0'
    return int(s)
class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        xs = version1.split('.')
        ys = version2.split('.')
        n = len(xs)-1
        m = len(ys)-1
        while n >= 0:
            if f(xs[n]) == 0:
                n -= 1
            else:
                break
        while m >= 0:
            if f(ys[m]) == 0:
                m -= 1
            else:
                break         
        n += 1
        m += 1
        i = 0
        j = 0
        while i < n and j < m:
            t1 = f(xs[i])
            t2 = f(ys[j])
            if t1 == t2:
                i += 1
                j += 1
            elif t1 < t2:
                return -1
            else:
                return 1
        if i < n:
            return 1
        if j < m:
            return -1
        return 0
