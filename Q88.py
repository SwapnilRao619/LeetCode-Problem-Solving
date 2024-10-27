## N
## Idea, approach and time complexity:
'''
The solution merges two sorted arrays, `nums1` and `nums2`, using a two-pointer technique starting from the end of the arrays. It compares the largest unmerged elements
and places them in the correct position in `nums1`, ensuring the final array remains sorted. If one array is exhausted, the remaining elements of the other are copied 
over. This approach runs in O(m + n) time, where `m` and `n` are the sizes of the two arrays, as each element is processed once.
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        x,y=m-1,n-1
        for i in range(m+n-1,-1,-1):
            if(x<0):
                nums1[i]=nums2[y]
                y-=1
            elif(y<0):
                break
            elif(nums1[x]>nums2[y]):
                nums1[i]=nums1[x]
                x-=1
            else:
                nums1[i]=nums2[y]
                y-=1