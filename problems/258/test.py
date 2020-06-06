class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        #1 2 3 4 5 6 7 8 9 1 
        #2 3 4 5 6 7 8 9 1 2
        if num == 0:
            return 0
        t = num%9
        return t if t > 0 else 9
