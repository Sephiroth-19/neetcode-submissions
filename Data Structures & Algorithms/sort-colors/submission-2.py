class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = 0
        b = 0
        c = len(nums)-1
        while b <= c:
            if nums[b] == 0:
                nums[a],nums[b] = nums[b],nums[a]
                a += 1
                b += 1
            elif nums[b] == 1:
                b += 1
            elif nums[b] == 2:
                nums[b],nums[c] = nums[c],nums[b]
                c -= 1
                