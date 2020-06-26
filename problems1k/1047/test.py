#20:05-20:06
class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        q = []
        for c in S:
            if len(q) == 0:
                q.append(c)
            elif q[len(q)-1] == c:
                q.pop()
            else:
                q.append(c)
        return ''.join(q)
