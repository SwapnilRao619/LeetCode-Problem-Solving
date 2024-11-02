## N
## Idea, approach and time complexity:
'''
The approach to determining if the last character in the `bits` list is a one-bit character involves iterating through the list while interpreting the bits. Each `0` 
signifies a one-bit character, while each `1` indicates a two-bit character. As we traverse the list, we advance one position for a `0` and two positions for a `1`.
After processing, we check if we land on the last bit of the list, which confirms whether it is indeed a one-bit character. The time complexity of this solution is O(n), 
where n is the length of the `bits` list, since we only make a single pass through the array.
'''

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i=0
        while(i<(len(bits)-1)):
            if(bits[i]==1):
                i+=2
            else:
                i+=1
        return i==(len(bits)-1)