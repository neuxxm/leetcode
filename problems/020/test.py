#11:59-12:03
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        q = []
        map = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c == '(' or c == '[' or c == '{':
                q.append(c)
            else:
                if len(q) == 0:
                    return False
                if q[len(q)-1] == map[c]:
                    q.pop()
                else:
                    q.append(c)
        return len(q) == 0
