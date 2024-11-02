## N
## Idea, approach and time complexity:
'''
The solution checks if the last character in a given binary array can be represented as a one-bit character. It iterates through the list, moving two indices forward 
when encountering a '1' (indicating a two-bit character) and one index forward for a '0'. The function returns `True` if it ends at the last index after processing, 
meaning the last character is indeed a one-bit character. The time complexity of this approach is O(n), where n is the length of the input list, as each element is 
processed at most once.
'''

class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i=0
        while(i<len(bits)):
            if(bits[i]==1):
                i+=2
            else:
                if(i==len(bits)-1):
                    return True
                else:
                    i+=1
        return False    
