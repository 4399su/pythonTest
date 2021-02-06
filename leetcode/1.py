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
                if i != nums.index(target - nums[i]):
                    return i, nums.index(target - nums[i])

    def copyTwosum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in nums:
                return i, dict[nums[i]]
            else:
                dict[nums[i]] = i
