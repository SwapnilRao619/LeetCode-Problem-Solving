## N
## Idea, approach and time complexity:
'''
The given code calculates the "score" of a string by summing the absolute differences in ASCII values between each consecutive character. The approach iterates through 
the string, comparing each pair of adjacent characters and adding the absolute difference to the score. The time complexity of this solution is O(n), where n is the 
length of the string, as it processes each pair of characters once.
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(not root):
            return
        temp=root.right
        root.right=root.left
        root.left=temp
        self.invertTree(root.right)
        self.invertTree(root.left)
        return root
