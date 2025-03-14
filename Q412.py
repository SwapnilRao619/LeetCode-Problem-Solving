## N
## Idea, approach and time complexity:
'''
The solution iterates through all integers from 1 to `n` and appends specific strings to a list based on divisibility conditions. If the number 
is divisible by both 3 and 5, it appends "FizzBuzz", if divisible by 3 only, it appends "Fizz", and if divisible by 5 only, it appends "Buzz". 
If neither, it appends the number itself as a string. This approach ensures that every number is checked and processed based on its divisibility. 
The time complexity of this solution is O(n) since it requires a single iteration over the range from 1 to `n`, where each check (modulus 
operation) is constant time. The space complexity is also O(n) due to the storage of the result list.
'''

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]
        for i in range(1,n+1):
            if(i%3==0 and i%5==0):
                ans.append("FizzBuzz")
            elif(i%3==0 and i%5!=0):
                ans.append("Fizz")
            elif(i%5==0 and i%3!=0):
                ans.append("Buzz")
            elif(i%3!=0 and i%5!=0):
                ans.append(str(i))
        return ans