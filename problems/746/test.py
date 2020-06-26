#6.26 20:52-21:08
def f(n, a, d, N):
    if n < 2:
        return a[n]
    if n < N and d[n] != -1:
        return d[n]
    t = min(f(n-1, a, d, N), f(n-2, a, d, N)) + a[n]
    d[n] = t
    return t
class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        cost.append(0)
        d = [-1] * (n+1)
        return f(n, cost, d, n)
