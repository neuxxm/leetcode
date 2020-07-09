#20:58-23:09
class trie_t:
    def __init__(self, val):
        self.sons = [None] * 26
        self.val = val
def add(td, s):
    cur = td
    l = len(s)
    for i in xrange(0, l):
        n = ord(s[i]) - ord('a')
        if cur.sons[n]:
            if i == l-1:
                cur.sons[n].val = 1
        else:
            if i != l-1:
                cur.sons[n] = trie_t(0)
            else:
                cur.sons[n] = trie_t(1)
        cur = cur.sons[n]
def find(td, s, i, s_len):
    cur = td
    rs = []
    while i < s_len:
        c = s[i]
        n = ord(c) - ord('a')
        if cur.sons[n]:
            cur = cur.sons[n]
            if cur.val == 1:
                rs.append(i)
            i += 1
        else:
            break
    return rs
def dfs(s, i, n, td, dp):
    if i >= n:
        return 0
    if dp[i] != -1:
        return dp[i]
    rs = find(td, s, i, n)
    if len(rs) == 0:
        z = dfs(s, i+1, n, td, dp) + 1
    else:
        z = dfs(s, i+1, n, td, dp) + 1
        for r in rs:
            t = dfs(s, r+1, n, td, dp)
            if t < z:
                z = t
    dp[i] = z
    #print s[i:], dp[i]
    return dp[i]
class Solution(object):
    def respace(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: int
        """
        ws = dictionary
        s = sentence
        td = trie_t(0)
        for w in ws:
            add(td, w)
        n = len(s)
        if n == 0:
            return 0
        dp = [-1] * n
        dfs(s, 0, n, td, dp)
        return dp[0]
