from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        i = 0 
        j = len(s) - 1
        ans = []       
        while j >= 0:
            ans.append(s[j])        
            print(s[j])     
            j -= 1
        return ans

sol = Solution()
s = ["H","a","n","n","a","h"]
print(sol.reverseString(s))