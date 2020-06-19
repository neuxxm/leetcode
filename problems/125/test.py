#11:04AC
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s2 = ''
        a = ord('a')
        z = ord('z')
        A = ord('A')
        Z = ord('Z')
        zero = ord('0')
        nine = ord('9')
        for c in s:
            n = ord(c)
            if a<=n and n<=z:
                s2 += c
            elif A<=n and n<=Z:
                s2 += chr(n-A+a)
            elif zero<=n and n<=nine:
                s2 += c
        b = True
        n = len(s2)
        t = n/2
        for i in xrange(0, t):
            if s2[i] != s2[n-1-i]:
                b = False
                break
        return b
