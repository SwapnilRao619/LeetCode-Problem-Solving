## Idea, approach and time complexity:
'''The idea behind this solution is to find the intersection of two arrays, `nums1` and `nums2`. The approach uses a set (`seen`) to store unique elements from `nums1`. 
Then, it iterates through `nums2` and checks if an element is present in the `seen` set and not yet added to the result list (`ans`). This ensures that the intersection 
is captured without duplicates. The time complexity is **O(m + n)**, where `m` and `n` are the lengths of `nums1` and `nums2`, respectively. This is because we loop 
through each array once to populate the set and check for intersections. The space complexity is **O(m)**, due to the storage used by the set for unique elements from 
`nums1`.'''

## Code:
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen=set()
        ans=[]
        for i in range(len(nums1)):
            if(nums1[i] not in seen):
                seen.add(nums1[i])
        for j in range(len(nums2)):
            if(nums2[j] in seen and nums2[j] not in ans):
                ans.append(nums2[j])
        return ans