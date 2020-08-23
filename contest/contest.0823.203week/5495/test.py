class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        c = [0] * (n+1)
        m = len(rounds)
        c[rounds[0]] = 1
        for i in xrange(1, m):
            start = rounds[i-1]+1
            end = rounds[i]
            if start <= end:
                for j in xrange(start, end+1):
                    c[j] += 1
            else:
                for j in xrange(start, n+1):
                    c[j] += 1
                for j in xrange(1, end+1):
                    c[j] += 1
        ma = 0
        mak = []
        for i in xrange(1, n+1):
            if c[i] > ma:
                ma = c[i]
                mak = []
                mak.append(i)
            elif c[i] == ma:
                mak.append(i)
        return mak
