## N
## Idea, approach and time complexity:
'''
The problem asks to find the diameter of a binary tree, which is defined as the length of the longest path between any two nodes in the tree. The diameter may pass 
through the root or lie entirely in one of the subtrees. To solve this, we use a depth-first search (DFS) approach to traverse the tree and calculate the height of each 
subtree. The height of a subtree is defined as the number of edges on the longest path from that node to a leaf node. During the DFS, for each node, we calculate the 
diameter by summing the heights of its left and right subtrees, and we keep track of the maximum diameter encountered. The key observation here is that the diameter of 
the tree at any node is simply the sum of the heights of its left and right subtrees, while the height of a node is 1 + max(height of left subtree, height of right 
subtree). We use a helper function height(root) which computes the height of the tree recursively while updating the global variable self.ld to store the largest 
diameter found so far. The recursion works by visiting each node in the tree, computing the height of its left and right children, and then calculating the possible 
diameter at that node. The recursive calls go down the tree, and each time they return, the diameter is updated based on the sum of the heights of the left and right 
subtrees. The base case for the recursion is when a node is None, where the height is returned as 0. The time complexity is O(N), where N is the number of nodes in the 
binary tree.
'''

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ld=0
        def height(root):
            if(not root):
                return 0
            lh=height(root.left)
            rh=height(root.right)
            d=lh+rh
            self.ld=max(d,self.ld)
            return 1+max(lh,rh)
        height(root)
        return self.ld