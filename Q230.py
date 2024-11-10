## N
## Idea, approach and time complexity:
'''
The approach is to perform an **inorder traversal** of the binary search tree (BST), which naturally visits nodes in ascending order. During this traversal, we collect 
node values in a list `ans`. After the traversal, the kth smallest element will be at the index `k-1` in the sorted list. The time complexity is **O(N)**, where `N` is 
the number of nodes in the tree, as we visit each node exactly once. The space complexity is also **O(N)** due to the storage of node values in the list `ans`.
'''

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans=[]
        def inorder(root):
            if(not root):
                return
            inorder(root.left)
            ans.append(root.val)
            inorder(root.right)
        inorder(root)
        return ans[k-1]