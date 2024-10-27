## N
## Idea, approach and time complexity:
'''
The provided solution defines a method to find the first palindrome in a list of words. It uses a helper function `isPalin` to check if a word reads the same forwards 
and backwards by comparing characters from both ends until they meet. The main function iterates through the list of words and returns the first palindrome found, or an 
empty string if none exist. The time complexity is O(n * m), where n is the number of words and m is the average length of the words, as each word needs to be checked
character by character.
'''

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        predef=""

        def isPalin(word):
            l,r=0,(len(word)-1)
            while(l<r):
                if(word[l]==word[r]):
                    l+=1
                    r-=1
                else:
                    return False
            return True

        for i in words:
            if(isPalin(i)==True):
                return i
        return predef