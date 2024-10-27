## N
## Idea, approach and time complexity:
'''
The function `differenceOfSum` calculates the absolute difference between the sum of elements in a list and the sum of their individual digits. It iterates through each 
number, accumulating the total sum of the numbers (`elesum`) and extracting digits for the digit sum (`digsum`). The approach uses a loop to break down numbers into 
their digits only when they are greater than or equal to 10. The overall time complexity is O(n * k), where n is the number of elements in the list and k is the maximum 
number of digits in any element, since each number may require multiple iterations to extract its digits.
'''

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        elesum,digsum=0,0
        digarr=[]
        for i in nums:
            elesum+=i
            if(i>=10):
                while(i>0):
                    digarr.append(i%10)
                    i=i//10
            elif(i<10):
                digarr.append(i)
        digsum=sum(digarr)
        return abs(digsum-elesum)