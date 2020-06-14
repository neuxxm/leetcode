#18:07-18:10
def count(s):
    cnt = 0
    last = ''
    r = ''
    for c in s:
        if c != last:
            if cnt > 0:
                r += '%d%s'%(cnt, last)
            last = c
            cnt = 1
        else:
            cnt += 1
    if cnt > 0:
        r += '%d%s'%(cnt, last)
    return r
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        for i in xrange(1, n):
            s = count(s)
        return s
