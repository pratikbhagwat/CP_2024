from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:

        maxWindow=0
        if  k==0:
            return self.longestOnesWithoutK(nums)

        i=j=0

        while j < len(nums):

            if k==0:
                if nums[j]==1:
                    j+=1
                else:
                    while nums[i] != 0:
                        i+=1
                    i+=1
                    k+=1

            else:
                if nums[j] == 1:
                    j+=1
                else:
                    k-=1
                    j+=1

            maxWindow = max(maxWindow,j-i)

        return maxWindow


    def longestOnesWithoutK(self, nums):

        i=j=0
        maxWindow = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                i=j
            maxWindow = max(maxWindow,j-i)
        return maxWindow


print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],k=3))