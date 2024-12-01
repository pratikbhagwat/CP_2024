from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxWindow=0
        for right in range(len(nums)):
            if k==0:
                if nums[right]==0:
                    while nums[left] != 0:
                        left+=1
                    left+=1
            else:
                if nums[right] == 0:
                    k-=1

            maxWindow = max(maxWindow,right-left+1)
        return maxWindow


    def longestOnesWithoutK(self, nums):

        left=0
        maxWindow = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                left=right
            maxWindow = max(maxWindow,right-left)
        return maxWindow


print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],k=3))