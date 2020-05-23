# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#10:20-10:50
def cut(s):
    i = 0
    n = len(s)
    cnt = 0
    buf = ''
    while i < n:
        if s[i] == '-':
            cnt += 1
        else:
            if cnt > 0:
                buf += '-' * (cnt-1)
                cnt = 0
            buf += s[i]
        i += 1
    return buf
class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        n = len(S)
        if n == 0:
            return None
        S = '^' + S + '-#'
        n = len(S)
        i = 0
        start = 1
        r = []
        while i < n-1:
            if S[i-1] != '-' and S[i] == '-' and S[i+1] != '-':
                end = i
                r.append(S[start:end])
                start = i + 1
            i += 1
        r_len = len(r)
        root = None
        if r_len == 1:
            root = TreeNode(int(r[0]))
        elif r_len == 2:
            root = TreeNode(int(r[0]))
            root.left = self.recoverFromPreorder(cut(r[1]))
        elif r_len == 3:
            root = TreeNode(int(r[0]))
            root.left = self.recoverFromPreorder(cut(r[1]))
            root.right = self.recoverFromPreorder(cut(r[2]))
        return root
