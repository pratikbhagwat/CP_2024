from typing import List
import heapq as pq

class Solution:
    def findKthLargest(self, nums: List[int], k: int):
        maxHeap= [-num for num in nums]
        pq.heapify(maxHeap)
        element=None
        while k!=0:
            element=pq.heappop(maxHeap)
            k-=1
        return element

    def findKthLargestUsingQuickSelect(self, nums: List[int], k):
        """

        :param nums:
        :return:


        partition algo
        """

        l=0
        r=len(nums)-1

        while l <= r:
            pivotIndex = self.partition(l, r, nums)
            if pivotIndex == len(nums)-k:
                return nums[pivotIndex]
            elif pivotIndex < len(nums)-k:
                l=pivotIndex+1
            else:
                r=pivotIndex-1



    def partition(self,l,r,nums):

        pivotElement=nums[r]
        pivotIndex=l
        if l == r:
            return r
        while l<r:
            if nums[l] <= pivotElement:
                nums[l], nums[pivotIndex] = nums[pivotIndex], nums[l]
                pivotIndex+=1

            l+=1

        nums[pivotIndex], nums[r] = nums[r], nums[pivotIndex]

        return pivotIndex




print(Solution().findKthLargestUsingQuickSelect([3,2,1,5,6,4], 2))
