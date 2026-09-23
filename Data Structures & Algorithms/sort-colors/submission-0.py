class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {
            0:0,
            1:0,
            2:0
        }
        for i in nums:
            if i == 0:
                count[0]+=1
            elif i == 1:
                count[1]+=1
            elif i == 2:
                count[2]+=1
        write = 0
        for _ in range(count[0]):
            nums[write] = 0
            write+=1
        for _ in range(count[1]):
            nums[write] = 1
            write+=1
        for _ in range(count[2]):
            nums[write] = 2
            write+=1
        return nums