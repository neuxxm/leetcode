#22:00-22:05
def f(a, i, n, dp):
    if dp[i] != -1:
        return dp[i]
    if i == n-1:
        return a[i]
    if i == n-2:
        dp[i] = max(a[n-2], a[n-1])
        return dp[i]
    dp[i] = max(f(a, i+1, n, dp), f(a, i+2, n, dp) + a[i])
    return dp[i]
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        if n == 0:
            return 0
        dp = [-1] * n
        return f(a, 0, n, dp)
