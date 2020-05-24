#17:04-17:22
import math
def f(label, lvl):
    return (1<<(lvl-1)) - label + (1<<lvl) - 1
class Solution(object):
    def pathInZigZagTree(self, label):
        """
        :type label: int
        :rtype: List[int]
        """
        lvl = int(log(label, 2)) + 1
        if lvl&1:
            real = label
        else:
            real = f(label, lvl)
        r = [0] * lvl
        r[lvl-1] = real
        for i in xrange(lvl-2, -1, -1):
            if r[i+1]&1:
                r[i] = (r[i+1]-1) >> 1
            else:
                r[i] = (r[i+1]) >> 1
        for i in xrange(lvl):
            if i&1:
                r[i] = f(r[i], i+1)
        return r
