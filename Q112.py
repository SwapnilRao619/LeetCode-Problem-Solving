## N
## Idea, approach and time complexity:
'''
The approach uses a depth-first search (DFS) to traverse the binary tree, starting from the root. At each node, it accumulates the sum of the node values and checks if a 
leaf node has been reached with the sum equal to the target. If any path results in the target sum, it returns `True`; otherwise, it returns `False`. The time complexity 
is O(N), where N is the number of nodes in the tree, as each node is visited once. The space complexity is O(H), where H is the height of the tree, due to the recursive 
call stack.
'''

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def ps(node, sumval):
            if(not node):
                return False
            sumval+=node.val
            if(not node.left and not node.right):
                return sumval==targetSum
            return ps(node.left,sumval) or ps(node.right,sumval)
        return ps(root,0)