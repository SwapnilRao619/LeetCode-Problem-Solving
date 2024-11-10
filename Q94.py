## N
## Idea, approach and time complexity:
'''
The given code implements the inorder traversal of a binary tree using recursion. It visits the left subtree, processes the root node, and then visits the right subtree. 
The algorithm follows the "Left, Root, Right" order, and it appends the values of the nodes to the result list `ans`. The time complexity is **O(n)**, where `n` is the 
number of nodes in the tree, because each node is visited exactly once. The space complexity is **O(h)**, where `h` is the height of the tree, due to the recursion stack.
'''

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        def inorder(root):
            if(not root):
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        return ans