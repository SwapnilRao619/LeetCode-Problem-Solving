## N
## Idea, approach and time complexity:
'''
The function `guessNumber` implements a binary search algorithm to efficiently find a target number between 1 and `n`. It repeatedly narrows down the search range by 
adjusting the low (`l`) and high (`h`) bounds based on the result of the `guess` function: if the guess is too low, it increases the lower bound; if too high, it 
decreases the upper bound. The time complexity of this approach is \(O(\log n)\) due to the halving of the search space in each iteration.
'''

class Solution:
    def guessNumber(self, n: int) -> int:
        l,h=1,n
        while(l<=h):
            m=(l+h)//2
            if(guess(m)>0):
                l=m+1
            elif(guess(m)<0):
                h=m-1
            else:
                return m