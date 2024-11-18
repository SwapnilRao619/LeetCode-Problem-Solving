## N
## Idea, approach and time complexity:
'''
The approach is straightforward: iterate through each word in the input list `words`, and for each word, check if the string `x` is a substring. If it is, append the 
index of that word to the result list `ans`. The time complexity of this solution is **O(n * m)**, where `n` is the number of words in the list and `m` is the average 
length of the words, due to the substring search operation (`x in words[i]`) being O(m) for each word.
'''

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        for i in range(len(words)):
            if(x in words[i]):
                ans.append(i)
        return ans