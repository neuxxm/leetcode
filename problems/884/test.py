#0:01-0:05
from collections import defaultdict
def f(a, b, r):
    map = defaultdict(lambda:0)
    map2 = defaultdict(lambda:0)
    for t in a:
        map[t] += 1
    for t in b:
        map2[t] += 1
    for k,v in map.items():
        if v == 1 and k not in map2:
            r.add(k)
    for k,v in map2.items():
        if v == 1 and k not in map:
            r.add(k)
class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        a = A.split(' ')
        b = B.split(' ')
        r = set()
        f(a, b, r)
        return list(r)
