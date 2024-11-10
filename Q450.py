## N
## Idea, approach and time complexity:
'''
The provided code implements a function to delete a node from a Binary Search Tree (BST). The `deleteNode` function follows a standard approach for deleting a node in a 
BST. First, it recursively searches for the node to delete by comparing the target key with the current node's value. If the key is smaller, the function proceeds to the 
left subtree; if the key is larger, it moves to the right subtree. Once the node to be deleted is found, three cases are handled: (1) If the node has no left child, it 
is replaced by its right child; (2) If the node has no right child, it is replaced by its left child; (3) If the node has both children, the function finds the minimum 
value node in the right subtree (successor), replaces the current node's value with the successor's value, and then deletes the successor node recursively. This 
approach ensures the BST property is maintained after the deletion. The time complexity of this algorithm is O(h), where h is the height of the tree. In the worst case, 
the tree can be unbalanced, leading to O(n) time, where n is the number of nodes. For a balanced tree, the time complexity is O(log n).
'''

class Solution:
    def minNode(self,root):
        if(not root):
            return None
        curr=root
        while(curr and curr.left):
            curr=curr.left
        return curr

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if(not root):
            return None
        if(key>root.val):
            root.right=self.deleteNode(root.right,key)
        elif(key<root.val):
            root.left=self.deleteNode(root.left,key)
        else:
            if(not root.right):
                return root.left
            elif(not root.left):
                return root.right
            else:
                minN=self.minNode(root.right)
                root.val=minN.val
                root.right=self.deleteNode(root.right,minN.val)
        return root