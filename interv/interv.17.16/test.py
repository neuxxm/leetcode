#23:43-23:50
def f(a, i, dp):
    if dp[i] != None:
        return dp[i]
    if i == 0:
        return a[i]
    if i == 1:
        dp[i] = max(a[0], a[1])
        return dp[i]
    dp[i] = max(f(a, i-1, dp), f(a, i-2, dp)+a[i])
    return dp[i]
class Solution(object):
    def massage(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        if n == 0:
            return 0
        dp = [None] * n
        return f(a, n-1, dp)
