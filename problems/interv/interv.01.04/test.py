class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {}
        for c in s:
            if c in map:
                map[c] += 1
            else:
                map[c] = 1
        cnt = 0
        for v in map.values():
            if v&1:
                cnt += 1
        return cnt <= 1
