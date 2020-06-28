class MyCalendarThree {
    public class SegmentTree {
        private class TreeNode {
            private int val;
            private int left;
            private int right;
            private TreeNode leftNode;
            private TreeNode rightNode;
            private int lazy;
            
            public TreeNode(int val, int left, int right) {
                this.val = val;
                this.left = left;
                this.right = right;
            }
            
            public int getMid() {
                return left + (right - left) / 2;
            }
            
            public TreeNode getLeft() {
                if(leftNode == null)
                    leftNode = new TreeNode(val, left, getMid());
                return leftNode;
            }
            
            public TreeNode getRight() {
                if(rightNode == null)
                    rightNode = new TreeNode(val, getMid() + 1, right);
                return rightNode;
            }
        }
        
        TreeNode root;
        public SegmentTree() {
            root = new TreeNode(0, 0, Integer.MAX_VALUE);
        }
        
        public int getMax() {
            return root.val;
        }
        
        public void update(int l, int r) {
            update(root, l, r, 0);
        }
        
        private void update(TreeNode node, int l, int r, int h) {
            if(node.lazy != 0) {
                node.val += node.lazy;
                if(node.leftNode != null) 
                    node.leftNode.lazy += node.lazy;
                if(node.rightNode != null) 
                    node.rightNode.lazy += node.lazy;
                node.lazy = 0;
            }
            
            if(node.left == l && node.right == r) {
                if(node.leftNode != null) 
                    node.leftNode.lazy++;
                if(node.rightNode != null) 
                    node.rightNode.lazy++;
                node.val++;
                return;
            }
            
            int mid = node.getMid();
            if(r <= mid) {
                update(node.getLeft(), l, r, h + 1);
            } else if(l > mid) {
                update(node.getRight(), l, r, h + 1);
            } else {
                update(node.getLeft(), l, mid, h + 1);
                update(node.getRight(), mid + 1, r, h + 1);
            }
            node.val = Math.max(node.getLeft().val + node.getLeft().lazy, node.getRight().val + node.getRight().lazy);
        }
    }
    
    private SegmentTree st;
    public MyCalendarThree() {
        st = new SegmentTree();
    }
    
    public int book(int start, int end) {
        st.update(start, end - 1);
        return st.getMax();
    }
}
