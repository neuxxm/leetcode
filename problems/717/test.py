#23:46-23:48
class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        a = bits
        n = len(a)
        i = 0
        b = False
        while i < n:
            if a[i] == 1:
                i += 2
                b = False
            else:
                i += 1
                b = True
        return b
