from typing import List

"""Find min in the rotated array"""
class Solution:
    def findMin(self, nums: List[int]) -> int:

        i=0
        j=len(nums)-1

        while(i<=j):
            mid = (i+j)//2

            if nums[mid]>nums[j]:
                i=mid+1
            else:

                if mid == 0 or nums[mid] < nums[mid-1]:
                    return nums[mid]
                else:
                    j=mid-1
        return nums[i]



    """Find max in the rotated array"""
    def findMax(self, nums: List[int]) -> int:

        i=0
        j=len(nums)-1

        while(i<=j):
            mid= (i+j)//2

            if nums[mid] < nums[i]:
                j=mid-1
            else:
                if mid == len(nums)-1 or nums[mid] > nums[mid+1]:
                    return nums[mid]
                else:
                    i=mid+1

        return nums[i]



print(Solution().findMax([3,4,5,1,2]))
