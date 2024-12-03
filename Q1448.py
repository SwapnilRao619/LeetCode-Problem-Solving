## N
## Idea, approach and time complexity:
'''
The approach in this solution is a depth-first search (DFS) that traverses the binary tree, keeping track of the maximum value encountered along the path from the root 
to each node. For each node, if its value is greater than or equal to the maximum value seen so far, it is considered a "good node." The function recursively visits the 
left and right children, updating the maximum value as it goes. The time complexity of this solution is O(n), where n is the number of nodes in the tree, because each 
node is visited exactly once. The space complexity is O(h), where h is the height of the tree, due to the recursion stack.
'''

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        def fgn(node,maxval):
            if(not node):
                return 0
            res=1 if maxval<=node.val else 0
            maxval=max(maxval,node.val)
            res+=fgn(node.left,maxval)
            res+=fgn(node.right,maxval)
            return res
        return fgn(root,root.val)