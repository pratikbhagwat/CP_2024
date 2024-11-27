

import bisect
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        index = bisect.bisect_left(nums, target)

        if index < len(nums) and nums[index]==target:
            return index

        return -1




print(Solution().search([-1,0,3,5,9,12], 9))