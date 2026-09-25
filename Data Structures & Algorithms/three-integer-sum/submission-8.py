class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        for a in range(len(nums)-2):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            left = a + 1
            right = len(nums)-1
            while left < right:
                if nums[a] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[a] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[a] + nums[left] + nums[right] == 0:
                    output.append([nums[a],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1

        return output