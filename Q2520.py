## N
## Idea, approach and time complexity:
'''
The solution counts how many digits in a given number `num` can divide the number itself without leaving a remainder. It first extracts the digits by repeatedly taking 
the last digit and dividing the number by 10. Then, it checks each digit to see if it divides the original number evenly, incrementing a count for each successful 
division. The time complexity is \(O(d)\), where \(d\) is the number of digits in the number, since each digit is processed individually.
'''

class Solution:
    def countDigits(self, num: int) -> int:
        numbers,copy,count=[],num,0
        while(num>0):
            numbers.append(num%10)
            num=num//10
        for i in numbers:
            if(copy%i==0):
                count+=1
        return count