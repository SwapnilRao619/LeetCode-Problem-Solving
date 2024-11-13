## N
## Idea, approach and time complexity:
'''
The problem aims to find the maximum beauty of items that can be bought with a given budget (query). To solve this, the approach involves first sorting the `items` list 
by price. Then, for each query (budget), we use binary search to efficiently find the most expensive item that can be bought within the budget, and track the highest 
beauty value seen so far for that price. We maintain a running maximum of the beauty values as we iterate through the sorted list to optimize querying. Each query 
searches for the most expensive item with a price ≤ the given budget, and for each such item, we update the maximum beauty. The time complexity is dominated by the 
sorting step (`O(n log n)`) and the binary search for each query (`O(log n)`), making the overall complexity `O(n log n + q log n)`, where `n` is the number of items and 
`q` is the number of queries.
'''

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items=sorted(items)
        ans=[]
        maxb=0
        for i in range(len(items)):
            maxb=max(maxb,items[i][1])
            items[i][1]=maxb
        for q in queries:
            maxb=0
            l,h=0,(len(items)-1)
            while(l<=h):
                m=(l+h)//2
                if(items[m][0]<=q):
                    maxb=max(maxb,items[m][1])
                    l=m+1
                else:
                    h=m-1
            ans.append(maxb)
        return ans