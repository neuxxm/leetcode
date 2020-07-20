#20:39-23:04
def fill(x, heap, z):
    for i in xrange(3):
        if heap[i] == None:
            heap[i] = x
            z[0] += 1
            return
        else:
            if x == heap[i]:
                return
def adjust(heap):
    cur = 0
    left = 1
    right = 2
    mi = heap[cur]
    mi_i = cur
    if heap[left] < mi:
        mi = heap[left]
        mi_i = left
    if heap[right] < mi:
        mi = heap[right]
        mi_i = right
    if mi_i == cur:
        return
    heap[cur], heap[mi_i] = heap[mi_i], heap[cur]
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heap = [None] * 3
        a = nums
        n = len(a)
        heap_size = [0]
        i = 0
        while i < n:
            fill(a[i], heap, heap_size)
            if heap_size[0] == 3:
                break    
            i += 1
        if heap_size[0] != 3:
            ma = 0
            for i in xrange(0, 3):
                if heap[i]:
                    if heap[i] > ma:
                        ma = heap[i]
            return ma
        map = {}
        for i in xrange(3):
            map[heap[i]] = 1
        adjust(heap)
        while i < n:
            if a[i] in map:
                i += 1
                continue
            if a[i] > heap[0]:
                del map[heap[0]]
                map[a[i]] = 1
                heap[0] = a[i]
                adjust(heap)
            i += 1
        return heap[0]
