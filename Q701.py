## N
## Idea, approach and time complexity:
'''
The solution inserts a value into a Binary Search Tree (BST) by recursively traversing the tree, comparing the value with the current node, and deciding whether to move 
left or right based on the comparison. If the appropriate spot is found (when the node is `None`), a new node with the given value is created and linked. This preserves 
the BST property where all left children are smaller and right children are larger than their parent. The time complexity is O(h), where `h` is the height of the tree, 
which could be O(n) in the worst case (unbalanced tree) or O(log n) in the best case (balanced tree).
'''

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if(not root):
            return TreeNode(val)
        if(val>root.val):
            root.right=self.insertIntoBST(root.right,val)
        elif(val<root.val):
            root.left=self.insertIntoBST(root.left,val)
        return root