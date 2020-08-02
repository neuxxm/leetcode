#16:44-17:28
from collections import defaultdict
def f(a, k, v):
    n = len(a)
    l = 0
    r = n - 1
    ans = -1
    while l <= r:
        m = (l+r) >> 1
        t = a[m]
        if k == t[0]:
            return
        if k < t[0]:
            ans = m
            r = m - 1
        else:
            ans = m+1
            l = m+1
    a.append(None)
    for i in xrange(n, ans, -1):
        a[i] = a[i-1]
    a[ans] = (k,v)
def find(a, k):
    n = len(a)
    l = 0
    r = n-1
    ans = -1
    while l <= r:
        m = (l+r) >> 1
        t = a[m]
        if k == t[0]:
            return t[1]
        if k < t[0]:
            ans = m
            r = m - 1
        else:
            ans = m+1
            l = m + 1
    if ans == -1:
        return ''
    else:
        ans -= 1
        if ans == -1:
            return ''
        # [2,4,6]
        # 1 0 -1
        # 3 1 0
        # 7 3 2
        return a[ans][1]
class TimeMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(list)
        
    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        map = self.map
        if key in map:
            f(map[key], timestamp, value)
        else:
            map[key].append((timestamp, value))
    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        map = self.map
        if key in map:
            return find(map[key], timestamp)
        else:
            return ''
