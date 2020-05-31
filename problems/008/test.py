class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str
        n = len(s)
        i = 0
        while i < n:
            if s[i] == ' ':
                i += 1
            else:
                break
        if i == n:
            return 0
        pos = 1
        if s[i] == '-':
            pos = -1
            i += 1
        elif s[i] == '+':
            i += 1
        elif s[i] not in set('0123456789'):
            return 0
        j = i
        while j < n:
            if s[j] in set('0123456789'):
                j += 1
            else:
                break
        if j == i:
            return 0
        r = 0
        l = 1
        int_max = (1<<31) - 1
        int_min = (1<<31)
        for k in xrange(j-1, i-1, -1):
            r += int(s[k]) * l
            if r > int_max and pos > 0:
                break
            elif r > int_min and pos < 0:
                break
            l *= 10      
        if pos > 0:
            if r > int_max:
                return int_max
            return r
        else:
            if r > int_min:
                return -int_min
            return r * pos
