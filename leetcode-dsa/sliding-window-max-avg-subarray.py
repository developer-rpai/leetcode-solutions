from typing import *
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_avg = sum(nums[:k])/k
        max_avg = window_avg

        for i in range(len(nums) - k ):
            window_avg = sum(nums[i:i+k])/k
            max_avg = max (window_avg, max_avg)

 


        return max_avg



sol = Solution()
nums = [1,12,-5,-6,50,3]
k = 4

print(sol.findMaxAverage(nums,k))