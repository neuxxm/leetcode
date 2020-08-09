#3:05-3:10
def f(rs, n, i, z):
    j = i-1
    r = 1
    while j>=0:
        if rs[j] == 1:
            r += 1
            j -= 1
        else:
            break
    j = i+1
    while j<n:
        if rs[j] == 1:
            r += 1
            j += 1
        else:
            break
    if r > z[0]:
        z[0] = r
class Solution(object):
    def reverseBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        n = num
        if n == 0:
            return 1
        rs = []
        while n != 0:
            rs.append(n&1)
            n >>= 1
        while len(rs) < 32:
            rs.append(0)
        l = len(rs)
        z = [0]
        for i in xrange(l):
            if rs[i] == 0:
                f(rs, l, i, z)
        return z[0]
