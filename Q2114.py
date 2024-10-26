## N
## Idea, approach and time complexity:
'''
The function `mostWordsFound` counts the number of words in each sentence by splitting the sentences on spaces and storing the counts in a dictionary. It then returns 
the maximum word count by sorting the values and accessing the last element. The time complexity is O(n * m), where n is the number of sentences and m is the average 
length of the sentences, due to the split operation and sorting the values.
'''

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        hm={}
        for i in sentences:
            hm[i]=len(i.split(" "))
        return sorted(hm.values())[-1]