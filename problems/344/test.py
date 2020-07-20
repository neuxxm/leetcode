#13:02-13:02
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
