## N
## Idea, approach and time complexity:
'''
The given solution defines a method to repeatedly sum the digits of a number until a single-digit result is obtained. The `checker` function extracts the digits and 
computes their sum, while the `addDigits` function invokes `checker` in a loop until the result is less than 10. The overall time complexity is O(d), where d is the 
number of digits in the input number, since each digit is processed separately. This approach effectively reduces the number through iterative digit summation.
'''

class Solution:
    def checker(self,num):
        track=[]
        while(num>0):
            track.append(num%10)
            num=num//10
        return sum(track)

    def addDigits(self, num: int) -> int:
        if(num<10):
            return num
        else:
            while(num>=10):
                num=self.checker(num)
        return num