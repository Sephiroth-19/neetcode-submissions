class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left) //2
            hour = 0
            for pile in piles:
                hour += (pile + mid - 1 )//mid	
            if hour <= h:
                #已经通过，寻找更小值
                right = mid
            else:
                #超过时间，需要增大k
                left = mid + 1
        return left
