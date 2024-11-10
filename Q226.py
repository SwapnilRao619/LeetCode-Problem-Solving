## N
## Idea, approach and time complexity:
'''
The solution inverts a binary tree by recursively swapping the left and right child nodes of each tree node. The approach starts at the root and for each node, it swaps 
the left and right subtrees, then recursively inverts both subtrees. This traversal continues until all nodes in the tree are visited and inverted. The time complexity 
of the algorithm is O(n), where n is the number of nodes in the tree, as each node is visited exactly once.
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(not root):
            return
        temp=root.right
        root.right=root.left
        root.left=temp
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root