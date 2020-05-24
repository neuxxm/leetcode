class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        need = {}
        cnt = {}
        str1 = 'aeiou'
        for c in str1:
            need[c] = 1
            cnt[c] = 0
        n = len(s)
        l = 0
        r = 0
        leng = 0
        ma = 0
        while r < n:
            c = s[r]
            if c in need:
                cnt[c] += 1
            r += 1
            leng += 1
            while leng == k:
                t = sum(cnt.values())
                if t > ma:
                    ma = t
                c = s[l]
                if c in need:
                    cnt[c] -= 1
                l += 1
                leng -= 1
        return ma
