class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        right = 0
        current_sum = 0
        current_len = 0
        min_len = 0
        while right < len(nums):
            current_sum += nums[right]
            while current_sum >= target:
                current_len = right - left + 1
                current_sum -= nums[left]
                left += 1
                if min_len == 0 and current_len > 0:
                    min_len = current_len
                elif min_len != 0 and current_len < min_len:
                    min_len = current_len
            right += 1
        return min_len