class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for j in range(len(nums)):
            if target - nums[j] in seen:
                return[seen[target - nums[j]],j]
            if nums[j] not in seen:
                seen[nums[j]] = j
                