## N
## Idea, approach and time complexity:
'''
The solution checks if a given integer `x` is a palindrome by first handling simple cases: if `x` is negative, it returns `False`, and if `x` is a single-digit number, 
it returns `True`. For numbers greater than 9, the algorithm uses a stack to store the digits of `x` by repeatedly taking the last digit (`x % 10`) and reducing `x` by 
dividing it by 10. After this, two pointers (`p` and `q`) are used to compare the digits from both ends of the stack. If any mismatch is found, the function returns 
`False`; otherwise, it returns `True`. The time complexity of this approach is O(n), where `n` is the number of digits in the integer `x`, since we traverse the digits 
once to store them in the stack and again to compare them. The space complexity is also O(n) due to the stack storing all digits.
'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        if(x<10):
            return True
        stack=[]
        while(x>0):
            stack.append(x%10)
            x//=10
        p,q=0,len(stack)-1
        while(p<q):
            if(stack[p]==stack[q]):
                p,q=p+1,q-1
            else:
                return False
        return True