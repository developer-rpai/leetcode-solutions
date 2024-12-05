from typing import *

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = curr = ans = 0

        for right in range(len(nums)):
            if nums[right] == 0 :
                curr += 1
            while curr > k:
                if nums[left] == 0 :
                    curr -= 1
                left += 1
            print("window len", right-left + 1)
            ans = max(ans, right-left+1)

        return ans


sol = Solution()
nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
k = 3
print(sol.longestOnes(nums, k))    