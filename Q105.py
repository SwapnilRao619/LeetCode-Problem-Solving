## N
## Idea, approach and time complexity:
'''
The solution constructs a binary tree from its preorder and inorder traversals by using recursion. The first element of the preorder list is the root, and its index in 
the inorder list splits the tree into left and right subtrees. The function then recursively builds the left and right subtrees by slicing the preorder and inorder lists 
accordingly. The time complexity is O(n^2) due to the repeated O(n) index lookups in the inorder list for each recursive call. This can be optimized to O(n) by using a 
hashmap to store the indices of elements in the inorder list, reducing the lookup time to O(1).
'''

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if(not preorder or not inorder):
            return
        root=TreeNode(preorder[0])
        mid=inorder.index(preorder[0])
        root.left=self.buildTree(preorder[1:mid+1],inorder[:mid])
        root.right=self.buildTree(preorder[mid+1:],inorder[mid+1:])
        return root