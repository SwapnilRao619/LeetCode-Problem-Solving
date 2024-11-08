## N
## Idea, approach and time complexity:
'''
The problem is to search for a given value in a Binary Search Tree (BST). The approach is to leverage the BST property: if the target value is greater than the current 
node's value, search the right subtree; if it is smaller, search the left subtree; otherwise, return the current node. The algorithm recursively narrows down the search 
space based on these comparisons. The time complexity is **O(h)**, where **h** is the height of the tree. In the worst case (unbalanced tree), **h** can be **O(n)**, 
and in the best case (balanced tree), it is **O(log n)**.
'''

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if(not root):
            return None
        else:
            if(val>root.val):
                return self.searchBST(root.right,val)
            elif(val<root.val):
                return self.searchBST(root.left,val)
            else:
                return root