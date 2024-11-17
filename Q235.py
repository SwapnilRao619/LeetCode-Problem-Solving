## N
## Idea, approach and time complexity:
'''
The approach used in this solution is based on the properties of a Binary Search Tree (BST). The algorithm recursively traverses the tree, starting from the root. At each 
step, it compares the values of nodes `p` and `q` with the current node (`root`). If both `p` and `q` are smaller, it moves to the left subtree, and if both are larger, 
it moves to the right subtree. The lowest common ancestor (LCA) is identified when `p` and `q` are on opposite sides of the current node, or one of them matches the 
current node. The time complexity of this approach is O(h), where h is the height of the tree, since in the worst case, we traverse from the root to a leaf node, and for 
a balanced tree, this would be logarithmic (`O(log n)`).
'''

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.lca=root
        def lcaHunt(root):
            self.lca=root
            if(p.val<root.val and q.val<root.val):
                lcaHunt(root.left)   
            elif(p.val>root.val and q.val>root.val):
                lcaHunt(root.right)
            else:
                return self.lca
        lcaHunt(root) 
        return self.lca