# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#18:10-18:36
def f(s):
    r = ''
    cnt = 0
    for c in s:
        if c == '-':
            cnt += 1
        else:
            if cnt > 0:
                r += '-'*(cnt-1)
                cnt = 0
            r += c
    if cnt > 0:
        r += '-'*(cnt-1)
    return r
class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        s = S
        n = len(s)
        n1 = n-1
        i = 1
        cnt = 0
        loc1 = -1
        loc2 = -1
        while i < n1:
            if s[i-1]!='-' and s[i] == '-' and s[i+1]!='-':
                cnt += 1
                if cnt == 1:
                    loc1 = i
                elif cnt == 2:
                    loc2 = i
            i += 1
        r = None
        if loc1 == -1:
            r = TreeNode(int(s))
        else:
            r = TreeNode(int(s[:loc1]))
            if loc2 == -1:
                r.left = self.recoverFromPreorder(f(s[loc1+1:]))
            else:
                r.left = self.recoverFromPreorder(f(s[loc1+1:loc2]))
                r.right = self.recoverFromPreorder(f(s[loc2+1:]))
        return r
