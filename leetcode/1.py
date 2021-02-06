from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

    def anTwosum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if target - nums[i] in nums:
                if i != nums[target - nums[i]].index:
                    return i, nums[target - nums[i]].index

    def copyTwosum(self,nums: List[int], target: int) -> List[int]:
        return
