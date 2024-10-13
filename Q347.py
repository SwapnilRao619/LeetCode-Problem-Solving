## N
## Idea, approach and time complexity:
'''
The provided solution counts the frequency of each number in the `nums` list using a hash map. It then sorts the frequency values and retrieves the top `k` most frequent 
elements by checking which keys in the hash map correspond to those frequencies. The time complexity is \(O(n \log n)\) due to the sorting step, where \(n\) is the 
number of unique elements in `nums`. The space complexity is \(O(n)\) for storing the frequency counts.
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm={}
        for i in nums:
            hm[i]=hm.get(i,0)+1
        count=(sorted(hm.values()))[-k:]
        return [key for key,value in hm.items() if value in count]