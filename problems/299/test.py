#20:09-20:13
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n = len(secret)
        x = secret
        y = guess
        a = 0
        b = 0
        map = {}
        for i in xrange(n):
            if x[i] == y[i]:
                a += 1
            else:
                t = x[i]
                if t in map:
                    map[t] += 1
                else:
                    map[t] = 1
        for i in xrange(n):
            if x[i] != y[i]:
                t = y[i]
                if t in map and map[t] > 0:
                    map[t] -= 1
                    b += 1
        return '%dA%dB'%(a, b)
