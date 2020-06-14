#20:52-20:55
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        n = len(image)
        m = len(image[0])
        a = image
        q = []
        q.append((sr, sc))
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        visit = {}
        visit[(sr,sc)] = 1
        while len(q) > 0:
            x,y = q.pop(0)
            ori = a[x][y]
            for i in xrange(4):
                x2 = x + dx[i]
                y2 = y + dy[i]
                if x2>=0 and x2<n and y2>=0 and y2<m:
                    if (x2,y2) not in visit and a[x2][y2] == ori:
                        q.append((x2,y2))
                        visit[(x2,y2)] = 1
            a[x][y] = newColor
        return a
