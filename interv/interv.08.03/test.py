#12:15-12:16
def update(ans, x):
    if ans == -1:
        ans = x
    elif x < ans:
        ans = x
    return ans
class Solution(object):
    def findMagicIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = nums
        n = len(a)
        if n == 0:
            return -1
        l = 0
        r = n-1
        ans = -1
        while l <= r:
            m = (l+r) >> 1
            if a[m] == m:
                ans = update(ans, a[m])
                r = m-1
            elif a[m] > m:
                if a[m]>=0 and a[m]<n:
                    if a[a[m]] == a[m]:
                        ans = update(ans, a[m])
                r = m-1
            else:
                if a[m]>=0 and a[m]<n:
                    if a[a[m]] == a[m]:
                        ans = update(ans, a[m])
                l = m+1
        return ans
