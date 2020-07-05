#22:40fail
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        r = ''
        while n != 0:
            t = n%26
            if t > 0:
                r += chr(t+ord('A')-1)
                n /= 26
            else:
                n /= 26
                if n > 0:
                    r += 'Z'
                    n -= 1
                else:
                    break
        return r[::-1]
