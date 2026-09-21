class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for a in range(len(nums)):
            for b in range(len(nums)):
                if nums[a] + nums[b] == target and a != b:
                    return [a,b]
             