## N
## Idea, approach and time complexity:
'''
The solution checks if a binary tree is balanced by recursively calculating the height of each subtree. It starts at the root and compares the heights of the left and 
right subtrees at each node. If the height difference exceeds 1 at any point, the tree is marked as unbalanced. This approach ensures that we can detect imbalances in a 
single pass through the tree. The time complexity is **O(n)**, where `n` is the number of nodes in the tree, as each node is visited once.
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced=True
        def height(root):
            if(not root):
                return 0
            lh=height(root.left)
            if(self.balanced==False):
                return 0
            rh=height(root.right)
            if(abs(lh-rh)>1):
                self.balanced=False
                return 0
            return (1+max(lh,rh))
        height(root)
        return self.balanced