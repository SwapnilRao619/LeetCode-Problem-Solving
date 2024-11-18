## N
## Idea, approach and time complexity:
'''
The solution decrypts a given list `code` based on a value `k`, where the decryption involves summing a specific set of elements in `code` for each index `i`. If `k > 0`, 
it sums the next `k` elements starting from index `i`, and if `k < 0`, it sums the previous `|k|` elements (by using modulo indexing to handle wrapping around the list). 
The approach iterates over all `n` elements, calculating the sum for each index using a nested loop. The time complexity is O(n * |k|), where `n` is the length of the 
list and `|k|` is the absolute value of `k`. This is because, for each of the `n` elements, it may compute a sum involving up to `|k|` elements.
'''

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        ans=[0]*n
        if(k==0):
            return ans
        for i in range(n):
            if(k>0):
                ans[i]=sum(code[(i+j)%n] for j in range(1,(k+1)))
            elif(k<0):
                ans[i]=sum(code[(i+j)%n] for j in range(k,0))
        return ans