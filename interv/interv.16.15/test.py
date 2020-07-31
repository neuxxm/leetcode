#0:33-0:34
from collections import defaultdict
class Solution(object):
    def masterMind(self, solution, guess):
        """
        :type solution: str
        :type guess: str
        :rtype: List[int]
        """
        a = solution
        b = guess
        n = len(solution)
        x = 0
        y = 0
        map = defaultdict(lambda:0)
        for i in xrange(n):
            if a[i] == b[i]:
                x += 1
            else:
                map[a[i]] += 1
        for i in xrange(n):
            if a[i] != b[i]:
                if b[i] in map and map[b[i]] > 0:
                    map[b[i]] -= 1
                    y += 1
        return [x, y]
