## N
## Idea, approach and time complexity:
'''
The given solution is for the "Best Time to Buy and Sell Stock" problem, where the goal is to maximize profit by buying and selling at different days, with the condition 
that you must buy before selling. The approach used here is a greedy one. We maintain two pointers: `p` (representing the day to buy) and `q` (representing the day to 
sell). The algorithm iterates through the list of prices, and if the current price (`prices[q]`) is less than the price on the day to buy (`prices[p]`), we update `p` to 
be `q`, since a lower price might lead to a higher profit later. If the current price is greater than the price on the buy day, we calculate the profit (`diff = prices[q] 
- prices[p]`) and update the maximum profit (`maxi`) if this new profit is larger than the previous one. This continues until all prices are evaluated. The time 
complexity of this approach is **O(n)**, where `n` is the length of the prices list, because we are iterating through the list just once. The space complexity is **O(1)**
, as only a constant amount of extra space is used.
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        p,q=0,1
        maxi=0
        while(q<len(prices)):
            if(prices[q]<prices[p]):
                p=q
            else:
                diff=prices[q]-prices[p]
                maxi=max(maxi,diff)
            q+=1
        return maxi