#14:19fail
import bisect
class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        a = []
        for x,y,h in buildings:
            a.append((x,-h,0))
            a.append((y,h,1))
        a.sort()
        heap = [0]
        r = []
        for x,h,c in a:
            if c == 0:
                h = -h
                if h > heap[len(heap)-1]:
                    r.append([x,h])
                    bisect.insort(heap, h)
                else:
                    bisect.insort(heap, h)
            else:
                t = heap[len(heap)-1]
                heap.remove(h)
                t2 = heap[len(heap)-1]
                if t2 != t:
                    r.append([x,t2])
            #print x,h,c, heap, r
        return r
