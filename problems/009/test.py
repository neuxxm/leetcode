#13:29
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        t = x
        if t == 0:
            return True
        if t < 0:
            return False
        n = 0
        while t > 0:
            n += 1
            t /= 10
        q = []
        i = 0
        u = n/2
        t = x
        while t > 0:
            z = t%10
            if i < u:
                q.append(z)
            elif (n&1) and i == u:
                pass
            else:
                x = q.pop()
                if x != z:
                    return False
            i += 1
            t /= 10
        return True
