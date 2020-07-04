#20:34-21:03
def f(a, i, n, c, dp):
    if dp[i] != -1:
        return dp[i]
    if i == 0:
        dp[i] = min(c)
        return dp[i]
    #1
    r = f(a, i-1, n, c, dp) + c[0]
    #7
    t = c[1]
    j = i-1
    while j >= 0:
        if a[j] >= a[i]-6:
            j -= 1
        else:
            break
    if j != -1:
        t += f(a, j, n, c, dp)
    if t < r:
        r = t
    #30
    t = c[2]
    j = i-1
    while j >= 0:
        if a[j] >= a[i]-29:
            j -= 1
        else:
            break
    if j != -1:
        t += f(a, j, n, c, dp)
    if t < r:
        r = t
    dp[i] = r
    return r  
class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        n = len(days)
        if n == 0:
            return 0
        dp = [-1] * n
        return f(days, n-1, n, costs, dp)
