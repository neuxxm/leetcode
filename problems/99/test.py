# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        cur = root
        last_d = -1
        last_node = None
        node1 = None
        node2 = None
        cnt = 0
        while cur:
            if cur.left == None:
                #print cur.val
                if cur.val < last_d:
                    if node1 == None:
                        node1 = last_node
                        node2 = cur
                    else:
                        node2 = cur
                last_d = cur.val
                last_node = cur
                cur = cur.right
            else:
                t = cur.left
                while t.right != None and t.right != cur:
                    t = t.right
                if t.right != cur:
                    t.right = cur
                    cur = cur.left
                else:
                    t.right = None
                    #print cur.val
                    if cur.val < last_d:
                        if node1 == None:
                            node1 = last_node
                            node2 = cur
                        else:
                            node2 = cur
                    last_d = cur.val
                    last_node = cur
                    cur = cur.right
        if node1 != None and node2 != None:
            t = node1.val
            node1.val = node2.val 
            node2.val = t
        return root
