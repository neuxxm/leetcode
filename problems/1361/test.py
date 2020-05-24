#13:49-14:01pending,15:23-15:33AC
def f(x, left, right, visit):
    if visit[x]:
        visit[x] = 2
        return True
    visit[x] = 1
    if left[x] != -1:
        if left[x] == x:
            visit[x] = 2
            return True
        if f(left[x], left, right, visit):
            return True
    if right[x] != -1:
        if right[x] == x:
            visit[x] = 2
            return True
        if f(right[x], left, right, visit):
            return True
    return False
class Solution(object):
    def validateBinaryTreeNodes(self, n, leftChild, rightChild):
        """
        :type n: int
        :type leftChild: List[int]
        :type rightChild: List[int]
        :rtype: bool
        """
        visit = [0] * n
        for i in xrange(n):
            for j in xrange(n):
                visit[j] = 0
            b = f(i, leftChild, rightChild, visit)
            if b:
                return False
            r = 0
            for v in visit:
                if v == 1:
                    r += 1
            if r == n:
                return True
        return False
