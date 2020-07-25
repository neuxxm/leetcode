#11:56-12:00
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        n = N
        ind = [0] * (n+1)
        outd = [0] * (n+1)
        ps = trust
        for p in ps:
            a = p[0]
            b = p[1]
            outd[a] += 1
            ind[b] += 1
        cnt = 0
        ans = -1
        for i in xrange(1, n+1):
            if outd[i] == 0 and ind[i] == n-1:
                ans = i
                cnt += 1
        return ans if cnt == 1 else -1
