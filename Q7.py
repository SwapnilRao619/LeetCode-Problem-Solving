## N
## Idea, approach and time complexity:
'''
The solution reverses the digits of an integer by first handling its sign, then extracting digits using a stack. The digits are joined and the result is checked to ensure 
it fits within the 32-bit integer range. If valid, it's returned; otherwise, 0 is returned. Time complexity is O(log(x)) due to the digit extraction process, and space 
complexity is O(log(x)) for storing the digits in the stack.
'''

class Solution:
    def reverse(self, x: int) -> int:
        if(x==0):
            return 0
        sign=-1 if x<0 else 1
        x=abs(x)
        stack=[]
        while(x>0):
            stack.append(x%10)
            x//=10
        num=sign*(int(''.join(map(str,stack))))
        if(num>=(-2**31) and num<=((2**31)-1)):
            return num
        return 0