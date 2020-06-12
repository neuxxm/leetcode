def f(a, i, n, path, lvl, r, map):
    if i == n:
        r.append(''.join(path[:lvl]))
        return
    for v in map[a[i]]:
        path[lvl] = v
        f(a, i+1, n, path, lvl+1, r, map)
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        a = digits
        n = len(a)
        if n == 0:
            return []
        map = {}
        map['2'] = 'abc'
        map['3'] = 'def'
        map['4'] = 'ghi'
        map['5'] = 'jkl'
        map['6'] = 'mno'
        map['7'] = 'pqrs'
        map['8'] = 'tuv'
        map['9'] = 'wxyz'
        path = [''] * n
        r = []
        f(a, 0, n, path, 0, r, map)
        return r
